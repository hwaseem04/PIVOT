from pathlib import Path
import yaml
from typing import Optional
import dashscope
from dashscope import VideoSynthesis
from http import HTTPStatus

class Wanxiang_video():
    """Parameters when called: img_path_lst, prompt, format_check."""

    def __init__(self,
                 config_path: Path = Path("config.yml"),
                 model: Optional[str] = None
                 ):
        if config_path is not None:
            with open(config_path, "r") as f:
                self.cfg: dict = yaml.safe_load(f)
        else:
            self.cfg = None
        self.api_key = self.cfg["alibaba"]["API_KEY"]
        if model is None:
            self.model = self.cfg["alibaba"]["T2V_MODEL"]
        else:
            self.model = model
        self.video_size = self.cfg["alibaba"]["IMAGE_SIZE"]

        # Set Base URL for International Usage
        dashscope.base_http_api_url = "https://dashscope-intl.aliyuncs.com/api/v1"
        dashscope.api_key = self.api_key

    def query(self, prompt: str):
        print(f"Generating video with model {self.model}...")
        try:
            rsp = VideoSynthesis.call(
                api_key=self.api_key,
                model=self.model,
                prompt=prompt,
                size="1280*720",
                n=1
            )
            
            if rsp.status_code == HTTPStatus.OK:
                video_url = rsp.output.video_url
                print(f"Video generated successfully: {video_url}")
                return video_url
            else:
                print(f"Video generation failed: {rsp.code}, {rsp.message}")
                return None
        except Exception as e:
            print(f"Exception during video generation: {e}")
            return None
