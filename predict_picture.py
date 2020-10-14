import numpy as np
import torch
from blazeface import BlazeFace
import cv2

net_blazeface: BlazeFace = None


def load_weights_blazeface(device: str = None) -> 'BlazeFace':
    if device not in ["cuda:0", "cpu"]:
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    net = BlazeFace().to(device)
    net.load_weights("blazeface.pth")
    net.load_anchors("anchors.npy")

    # Optionally change the thresholds:
    net.min_score_thresh = 0.75
    net.min_suppression_threshold = 0.3

    return net


def detect_picture(img):
    global net_blazeface

    if not net_blazeface:
        net_blazeface = load_weights_blazeface()

    img = cv2.imread(img)
    img = cv2.resize(img, (128, 128))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    detections = net_blazeface.predict_on_image(img)

    return detections