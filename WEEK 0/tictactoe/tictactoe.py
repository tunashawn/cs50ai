"""
tictactoe Player
"""
import copy
import random
import time
from curses.ascii import EM
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0
    for rows in board:
        x = x + rows.count(X)
        o = o + rows.count(O)
    return O if o < x else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    list = []
    x = 0
    while x < 3:
        y = 0
        while y < 3:
            if board[x][y] == EMPTY:
                list.append((x, y))
            y = y + 1
        x = x + 1
    return list


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    x = action[0]
    y = action[1]
    if board[x][y] == EMPTY:
        board[x][y] = X if player(board) == X else O
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for x in range(3):
        if board[x][0] == board[x][1] == board[x][2]:
            return board[x][0]
        elif board[0][x] == board[1][x] == board[2][x]:
            return board[0][x]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    elif len(actions(board)) == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    won = winner(board)
    if won is None:
        return 0
    elif won == X:
        return 100
    else:
        return -100


def minimax(board):
    """
    This method uses minimax with alpha beta pruning to optimize the running time
    Returns the optimal action for the current player on the board.
    """
    b = copy.deepcopy(board)  # Deep copy the board to test moves
    if player(board) == X:
        move, val = max_val_pruning(b, 0, -math.inf, math.inf)
    else:
        move, val = min_val_pruning(b, 0, -math.inf, math.inf)
    return move


def max_val_pruning(board, depth, alpha, beta):
    """
    :param board: the board
    :param depth: depth of the search tree
    :param alpha: alpha value
    :param beta: beta value
    :return: move and value of that move
    """
    if terminal(board):  # If the game is ended
        val = utility(board)  # Get the score
        if val == -100:
            return None, val + depth  # As the depth increase, the value for O win increase
        elif val == 100:
            return None, val - depth  # AS the depth increase, the value for X win decrease
        else:
            return None, val

    val = - math.inf  # Set the initial value for the best value
    move = None
    # For each possible action on the board
    for a in actions(board):
        # Get the move (temp, won't be used) and value for the given action
        m, v = min_val_pruning(result(copy.deepcopy(board), a), depth + 1, alpha, beta)
        # Case the value for the given action if greater than the best value
        if v > val:
            val = v  # Set the new best value
            move = a  # Set the best move
            alpha = max(alpha, val)  # Set the alpha value
        # Random choose between actions that have the same value as the best value
        # So the AI won't move the same way in the same scenario
        elif v == val and bool(random.getrandbits(1)):
            move = a
        # Stop exploring if the best value of this action is greater than beta value
        if val > beta:
            return move, val
    return move, val


def min_val_pruning(board, depth, alpha, beta):
    if terminal(board):
        val = utility(board)
        if val == -100:
            return None, val + depth
        elif val == 100:
            return None, val - depth
        else:
            return None, val
    val = math.inf
    move = None
    for a in actions(board):
        m, v = max_val_pruning(result(copy.deepcopy(board), a), depth + 1, alpha, beta)
        if v < val:
            val = v
            move = a
            beta = min(beta, val)
        elif v == val and bool(random.getrandbits(1)):
            move = a
        if val < alpha:
            return move, val
    return move, val
