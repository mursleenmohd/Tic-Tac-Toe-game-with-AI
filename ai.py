import math
import random
def check_winner(board):
    win_patterns = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for pattern in win_patterns:
        a, b, c = pattern
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

def minimax(board, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == "O": return 1
    if winner == "X": return -1
    if winner == "Draw": return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                eval = minimax(board, False, alpha, beta)
                board[i] = ""
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                eval = minimax(board, True, alpha, beta)
                board[i] = ""
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def get_best_move(board, level="Hard"):
    empty = [i for i, val in enumerate(board) if val == ""]
    if level == "Easy":
        return random.choice(empty) if empty else None
    elif level == "Medium":
        return random.choice(empty) if random.random() < 0.5 else _best_move(board)
    return _best_move(board)

def _best_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, False, -math.inf, math.inf)
            board[i] = ""
            if score > best_score:
                best_score = score
                best_move = i
    return best_move
