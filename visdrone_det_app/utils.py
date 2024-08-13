import os
from ultralytics import YOLO
from PIL import Image
from visdrone_det_app.settings import config


BASEDIR = os.path.abspath(os.path.dirname(__file__))


def build_image_path(image_file_name, directory="images/uploads"):
    return os.path.join(
                BASEDIR, "static", directory, image_file_name
                )


def process_image(image_file_name):
    model = YOLO(f"{BASEDIR}/models/{config.MODEL_NAME}")
    image_path = build_image_path(image_file_name)
    image = Image.open(image_path).convert('RGB')
    result = model(image)
    result[0].save(filename=build_image_path(image_file_name, "images/predictions"))