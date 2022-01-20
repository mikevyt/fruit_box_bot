from drag import drag


def solve(board):
    score = 0
    i = 0
    while i < len(board):
        j = 0
        while j < len(board[i]):
            if board[i][j] == 0:
                j += 1
                continue
            a = i

            while a < len(board) + 1:
                b = j
                while b < len(board[i]) + 1:
                    total = drag_sum(board, i, j, a, b)
                    if total == 10:
                        board = make_move(board, i, j, a, b)
                        score += 1
                        break
                    elif total > 10:
                        break
                    b += 1
                a += 1
            j += 1
        i += 1

    return score, board


def drag_sum(board, i, j, a, b):
    total = 0
    for c in range(i, a):
        for d in range(j, b):
            total += board[c][d]
    return total


def make_move(board, i, j, a, b):
    drag(i, j, a, b)
    for c in range(i, a):
        for d in range(j, b):
            board[c][d] = 0
    return board
