import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def compare_images(img1, img2):

    img1 = cv2.resize(img1, (224,224))
    img2 = cv2.resize(img2, (224,224))

    hist1 = cv2.calcHist(
        [img1],
        [0,1,2],
        None,
        [8,8,8],
        [0,256,0,256,0,256]
    )

    hist2 = cv2.calcHist(
        [img2],
        [0,1,2],
        None,
        [8,8,8],
        [0,256,0,256,0,256]
    )

    cv2.normalize(hist1,hist1)
    cv2.normalize(hist2,hist2)

    color_similarity = cv2.compareHist(
        hist1,
        hist2,
        cv2.HISTCMP_INTERSECT
    )

    structure_score = ssim(
        img1,
        img2,
        channel_axis=2
    )

    score = (
        0.5 * color_similarity +
        0.5 * structure_score
    )

    return score
