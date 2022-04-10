import time
import pprint
from parse_board import parse_board_from_screenshot
from solver import solve


def main():
    time.sleep(2)  # Time to open game window
    pp = pprint.PrettyPrinter(indent=4)
    board = parse_board_from_screenshot()
    
    score = 0
    trial_score = float('inf')
    while trial_score > 0:
        trial_score, board = solve(board)
        print(f'Trial: {trial_score}')
        score += trial_score
    pp.pprint(board)
    print(f'Score: {score}')


if __name__ == "__main__":
    main()
