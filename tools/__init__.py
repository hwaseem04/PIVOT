try:
    from .qwen_tts import Qwentts
    from .wanxiang_video import Wanxiang_video
    from .wanxiang_image import Wanxiang_image
except ImportError:
    pass
#from .gemini import GEMINI


__all__ = ["Qwentts", "Wanxiang_video","Wanxiang_image"]
