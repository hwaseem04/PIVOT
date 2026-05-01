from pathlib import Path
import yaml
from typing import Optional
import dashscope
from dashscope import ImageSynthesis
from http import HTTPStatus

class Wanxiang_image():
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
            self.model = self.cfg["alibaba"]["T2I_MODEL"]
        else:
            self.model = model
        # Using IMAGE_SIZE from config or default to 1024*1024
        self.image_size = self.cfg["alibaba"].get("IMAGE_SIZE", "1024*1024")

        # Set Base URL for International Usage
        dashscope.base_http_api_url = "https://dashscope-intl.aliyuncs.com/api/v1"
        dashscope.api_key = self.api_key

    def query(self, prompt: str):
        print(f"Generating image with model {self.model}...")
        try:
            rsp = ImageSynthesis.call(
                api_key=self.api_key,
                model=self.model,
                prompt=prompt,
                size=self.image_size,
                n=1
            )
            
            if rsp.status_code == HTTPStatus.OK:
                # Assuming single result
                if rsp.output.results:
                    image_url = rsp.output.results[0].url
                    print(f"Image generated successfully: {image_url}")
                    return image_url
                else:
                    print("Image generation succeeded but no results found.")
                    return None
            else:
                print(f"Image generation failed: {rsp.code}, {rsp.message}")
                return None
        except Exception as e:
            print(f"Exception during image generation: {e}")
            return None
