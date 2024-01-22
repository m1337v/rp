import threading
import numpy
from PIL import Image
from keras import Model

from roop.typing import Frame

PREDICTOR = None
THREAD_LOCK = threading.Lock()
MAX_PROBABILITY = 999

def get_predictor() -> Model:
    global PREDICTOR
    return PREDICTOR

def clear_predictor() -> None:
    global PREDICTOR
    PREDICTOR = None

def predict_frame(target_frame: Frame) -> bool:
    return False

def predict_image(target_path: str) -> bool:
    return False

def predict_video(target_path: str) -> bool:
    return False
