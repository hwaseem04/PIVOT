
from PIL import Image
import numpy as np
from moviepy.editor import VideoFileClip, AudioFileClip, vfx, ImageClip, CompositeVideoClip, concatenate_videoclips, AudioClip, concatenate_audioclips
from moviepy.video.fx import speedx  
import re
from pathlib import Path
import base64
import io
import subprocess
from pathlib import Path
from io import BytesIO
import os
from moviepy.video.io.ffmpeg_writer import ffmpeg_write_video

def add_silence(audio, target_duration):
    """Pad silence at the end of the audio so that its total length matches the target duration"""
    if audio.duration >= target_duration:
        return audio  
    silence = AudioClip(
        make_frame=lambda t: [0] * audio.nchannels,
        duration=target_duration - audio.duration,
        fps=audio.fps
    )
    return concatenate_audioclips([audio, silence])

def download_video(url: str, save_dir: str, custom_name=None):
    Path(save_dir).mkdir(parents=True, exist_ok=True)
    filename = custom_name
    save_path = Path(save_dir) / filename
    subprocess.run(["wget", "-O", str(save_path), url], check=True)
    return str(save_path.resolve())

def extract_key_frames(video_path):
    clip = VideoFileClip(str(video_path))
    duration = clip.duration

    # key time
    key_times = [duration / 4, duration / 2, 3 * duration / 4]

    key_frames = []
    last_valid_frame = None

    for t in key_times:
        try:
            # 真正按时间点读取帧
            frame_np = clip.get_frame(t)              # numpy.ndarray (H, W, 3)
            frame_img = Image.fromarray(frame_np)     # convert to PIL.Image
            key_frames.append(frame_img)
            last_valid_frame = frame_img
        except Exception as e:
            print(f"Error reading frame at {t:.2f} seconds: {e}")
            key_frames.append(last_valid_frame)       # use useful frame

    clip.close()
    return key_frames

def save_video(video_path, video ):
    clip = VideoFileClip(video)
    
    fps = clip.fps if clip.fps else 24.0
    audiofile = None
    if clip.audio:
        audiofile = str(video_path) + "_temp_audio.m4a"
        clip.audio.write_audiofile(audiofile, fps=44100, codec="aac", verbose=False, logger=None)
        
    ffmpeg_write_video(clip, video_path, fps, codec="libx264", audiofile=audiofile)
    if audiofile and os.path.exists(audiofile):
        os.remove(audiofile)

def convert_frame_to_base64(frame):
    image = Image.fromarray(np.uint8(frame))  
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format="JPEG")  
    img_byte_arr.seek(0)  
    
    b64code = base64.b64encode(img_byte_arr.read()).decode()
    return f"data:image/jpeg;base64,{b64code}"

def image_to_base64(image_paths):
    result = []
    for path in image_paths:
        with Image.open(path) as img:
            buffered = BytesIO()
            img.save(buffered, format="PNG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode()
            result.append(img_base64)
    return result 
    
def image_to_images(image_paths):
    """
    Read images from disk and return a list of PIL.Image objects.
    :param image_paths: list of image file paths
    :return: list of PIL.Image
    """
    images = []
    for path in image_paths:
        img = Image.open(path).convert("RGB")  # 统一为 RGB
        images.append(img)
    return images

def merge_video_audio(video_path, audio_path, text, path):
    number = float(re.search(r'\d+(?:\.\d+)?', str(text)).group())
    video_path = str(video_path)
    audio_path = str(audio_path)
    path = str(path)
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)

    video_dur = video.duration
    audio_dur = audio.duration
    # compute speed
    if video_dur >  number:
        speed = min(1.5, video_dur/number)
    else:
        speed = max(1 / 1.5, video_dur/number)

    video = vfx.speedx(video, factor=speed)
    audio_dur = audio.duration
    # if audio is longer, make video longer
    if audio_dur > video.duration:
        video = vfx.speedx(video, factor=video.duration / audio_dur)
    else:
        audio = add_silence(audio, video.duration)

    final = video.set_audio(audio)
    
    # Imports now global


    output_fps = video.fps
    if output_fps is None:
        print("Warning: video.fps is None, defaulting to 24 fps.")
        output_fps = 24.0
    output_fps = float(output_fps)
    
    print(f"DEBUG: Manual ffmpeg write with fps={output_fps}")
    
    # Manual audio writing
    audiofile = str(path) + "_temp_audio.m4a"
    final.audio.write_audiofile(audiofile, fps=44100, codec="aac", verbose=False, logger=None)
    
    # Manual video writing
    ffmpeg_write_video(final, str(path), output_fps, codec='libx264', audiofile=audiofile)
    final.close()
    
    if os.path.exists(audiofile):
        os.remove(audiofile)

def image_to_video(image_path, audio_path, video_duration, output_path):
    """
    merge video and audio
    :param image_path: video
    :param audio_path: audio
    :param video_duration: video duration
    :param output_path: video output path
    """
    image_path = str(image_path)
    audio_path = str(audio_path)
    output_path = str(output_path)
    video_duration = float(re.search(r'\d+(?:\.\d+)?', video_duration).group())

    video_duration = min(video_duration, 12)
    video_duration = max(video_duration, 4)

    # create ImageClip 
    image_clip = ImageClip(image_path, duration=video_duration)

    # get the height/width
    image_width, image_height = image_clip.size

    # set the resolution
    video_width, video_height = 1920, 1080

    # compute position
    x_center = (video_width - image_width) / 2
    y_center = (video_height - image_height) / 2

    # create ImageClip
    centered_image_clip = image_clip.set_position((x_center, y_center))

    # create a  CompositeVideoClip 
    video = CompositeVideoClip([centered_image_clip], size=(video_width, video_height))

    # save temp document
    temp_video_path = "temp_video.mp4"
    # Manual write to bypass decorator bugs
    ffmpeg_write_video(video, temp_video_path, 24.0, codec='libx264', audiofile=None)

    # use merge_video_audio to adjust time duration
    merge_video_audio(temp_video_path, audio_path, video_duration, output_path)

    # close
    video.close()
    image_clip.close()

def concatenate_videos(video_list, output_path):
    """Concatenate scene videos into a single output video via ffmpeg concat demuxer.

    Uses ffmpeg directly (not MoviePy) to avoid MoviePy audio-loss bugs caused by
    concatenate_videoclips(method="compose") producing a CompositeVideoClip whose
    audio is dropped by ffmpeg_write_video.

    ffmpeg concat demuxer:
      - Copies the video stream without re-encoding (-c:v copy, fast & lossless).
      - Explicitly encodes audio as AAC (-c:a aac), preserving it in the .mp4.
    """
    output_path = str(output_path)
    concat_file  = output_path + "_concat_list.txt"

    try:
        # Build the ffmpeg concat input file (one "file 'path'" line per scene)
        with open(concat_file, "w") as f:
            for video_path in video_list:
                # Escape single-quotes in paths for ffmpeg concat syntax
                safe_path = str(video_path).replace("'", "'\\''")
                f.write(f"file '{safe_path}'\n")

        subprocess.run(
            [
                "ffmpeg", "-y",
                "-f", "concat",
                "-safe", "0",
                "-i", concat_file,
                "-c:v", "copy",          # copy video stream — no re-encode needed
                "-c:a", "aac",           # encode audio as AAC (compatible with .mp4)
                "-movflags", "+faststart",
                output_path,
            ],
            check=True,
            capture_output=True,
        )
    finally:
        if os.path.exists(concat_file):
            os.remove(concat_file)
if __name__ == "__main__":
    plan = {"scenario":"1",
            "prompt":"1",
            }
    video_path = extract_key_frames("C:\\Users\\87719\\Desktop\\AgenticIR-main\\output\\example\\scene_0\\videos\\1080p60\\scene.mp4" )




