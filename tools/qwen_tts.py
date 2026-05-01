import os
import dashscope.audio
from pathlib import Path
import yaml

class Qwentts:
    def __init__(self, config_path: Path = Path("config.yml"),):
        
        if config_path is not None:
            with open(config_path, "r") as f:
                self.cfg: dict = yaml.safe_load(f)
        else:
            self.cfg = None
        self.api_key = self.cfg["alibaba"]["API_KEY"]
        self.headers = {
            "Content-Type": "application/json",
            "x-api-key": self.api_key,
        }
        
        # Set Base URL for International Usage (UAE/Outside China)
        dashscope.base_url = "https://dashscope-intl.aliyuncs.com/api/v1"
        dashscope.base_http_api_url = "https://dashscope-intl.aliyuncs.com/api/v1"
        dashscope.api_key = self.api_key
    def return_audio(self, text):
        model = self.cfg["alibaba"].get("VOICE_MODEL", "qwen-tts")
        voice = self.cfg["alibaba"].get("VOICE", "Aiden")
        speech_rate = self.cfg["alibaba"].get("speech_rate", 1.0)
        
        # Determine if model supports 'speech_rate' parameter directly
        # For qwen-tts-v2 and later, speech_rate is supported.
        # For some specific new models, it might be 'parameters' dict.
        # Based on DashScope docs for python SDK, typically passed as speech_rate
        
        response = dashscope.audio.qwen_tts.SpeechSynthesizer.call(
            model=model,
            api_key=self.api_key,
            text=text,
            voice=voice,
            speech_rate=speech_rate
        )
        
        if response.status_code == 200:
             return response["output"]["audio"]["url"]
        else:
             print(f"Error during TTS generation: {response}")
             raise RuntimeError(f"TTS Model ({model}) failed: {response.message}")
    



    