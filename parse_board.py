import pyscreenshot as ImageGrab
from constants import BOARD_TOP_BOUND, BOARD_LEFT_BOUND, NUMBER_HEIGHT, NUMBER_WIDTH, GAP_WIDTH, GAP_HEIGHT
import numpy as np
import os
from PIL import Image


def parse_board_from_screenshot():
    top_bound = BOARD_TOP_BOUND
    board = [[0 for _ in range(17)] for _ in range(10)]

    # Vertical
    for i in range(10):
        left_bound = BOARD_LEFT_BOUND
        bottom_bound = top_bound + NUMBER_HEIGHT
        # Horizontal
        for j in range(17):
            right_bound = left_bound + NUMBER_WIDTH
            im = ImageGrab.grab(bbox=(left_bound, top_bound, right_bound, bottom_bound))
            num = get_number_from_image(im)
            board[i][j] = int(num)
            left_bound = right_bound + GAP_WIDTH
        top_bound = bottom_bound + GAP_HEIGHT
    return board


def get_number_from_image(image):
    for filename in os.listdir('number_images'):
        f = os.path.join('number_images', filename)
        known_image = Image.open(f)
        if image_compare(image, known_image):
            # Files are labelled by their number
            return filename[0]


def image_compare(image_1, image_2):
    arr1 = np.array(image_1)
    arr2 = np.array(image_2)
    if arr1.shape != arr2.shape:
        return False
    maxdiff = np.max(np.abs(arr1 - arr2))
    return maxdiff == 0
