import pyautogui
from constants import BOARD_TOP_BOUND, BOARD_LEFT_BOUND, NUMBER_HEIGHT, NUMBER_WIDTH, GAP_WIDTH, GAP_HEIGHT


def drag(i, j, a, b):
    start_x = BOARD_LEFT_BOUND + j * (NUMBER_WIDTH + GAP_WIDTH) - GAP_WIDTH / 2
    start_y = BOARD_TOP_BOUND + i * (NUMBER_HEIGHT + GAP_HEIGHT) - GAP_HEIGHT / 2
    dx = (b - j) * (NUMBER_WIDTH + GAP_WIDTH)
    dy = (a - i) * (NUMBER_HEIGHT + GAP_HEIGHT)
    pyautogui.moveTo(start_x / 2, start_y / 2)
    pyautogui.mouseDown(button='left')
    pyautogui.move(dx / 2, dy / 2)
    pyautogui.mouseUp(button='left')
