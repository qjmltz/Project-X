import sys
import os

from face_alignment import mtcnn
import argparse
from PIL import Image
from tqdm import tqdm
import random
from datetime import datetime
mtcnn_model = mtcnn.MTCNN(device='cuda:0', crop_size=(112, 112))

def add_padding(pil_img, top, right, bottom, left, color=(0,0,0)):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

def get_aligned_face(image_path, rgb_pil_image=None):
    if isinstance(image_path, str):
        img = Image.open(image_path).convert('RGB')
    elif isinstance(image_path, Image.Image):
        img = image_path.convert('RGB')
    else:
        raise ValueError("Input must be a path string or PIL.Image.Image")

    try:
        bboxes, faces = mtcnn_model.align_multi(img, limit=1)
        face = faces[0]
    except Exception as e:
        # print('Face detection Failed due to error.')
        # print(e)
        face = None

    return face


