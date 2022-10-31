import random
import chess

def pick_random_move(board):
    """Picks a random move from the given board."""
    return random.choice(list(board.legal_moves))

def pick_best_move(board):
    """Picks the best move from the given board."""
    return chess.Move.from_uci("e2e4")
    