import pyscreenshot as ImageGrab
import pytesseract
from constants import BOARD_TOP_BOUND, BOARD_LEFT_BOUND, NUMBER_HEIGHT, NUMBER_WIDTH, GAP_WIDTH, GAP_HEIGHT


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
            num = pytesseract.image_to_string(im, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=123456789')
            board[i][j] = int(num)
            left_bound = right_bound + GAP_WIDTH
        top_bound = bottom_bound + GAP_HEIGHT
    return board
