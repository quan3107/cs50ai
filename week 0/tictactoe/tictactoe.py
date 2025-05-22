"""
Tic Tac Toe Player
"""

import math
import copy

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
    numOfX = sum([row.count(X) for row in board])
    numOfO = sum([row.count(O) for row in board])
    if numOfX > numOfO:
        return O
    elif numOfX == numOfO:
        return X
    else:
        return 0


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    results = set()
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == EMPTY:
                results.add((i, j))
    return results

            


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid action")
    
    newState = copy.deepcopy(board)
    newState[action[0]][action[1]] = player(board)

    return newState




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if [board[0][0], board[1][1], board[-1][-1]].count(X) == 3 or [board[0][-1], board[1][1], board[-1][0]].count(X) == 3:
        return X
    elif  [board[0][0], board[1][1], board[-1][-1]].count(O) == 3 or [board[0][-1], board[1][1], board[-1][0]].count(O) == 3:
        return O
    else:
        for i in range(0, len(board)):
            
            
                for j in range(0, len(board[i])):
                    if [item for item in board[i]].count(X) == 3:
                        return X
                    elif [item for item in board[i] ].count(O) == 3:
                        return O
                    elif [board[c][j] for c in range(0, len(board))].count(X) == 3:
                        return X
                    elif  [board[c][j] for c in range(0, len(board))].count(O) == 3:
                        return O
                    else:
                        continue

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    total = sum([row.count(X) for row in board]) + sum([row.count(O) for row in board])
    
    if (total== 9) or (winner(board) is not None):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def maxValue(board):
    v = -math.inf
    vMax = (v, ())
    
    if terminal(board):
        return (utility(board), None)
        #return utility(board)
    for action in actions(board):
        v = max(v, minValue(result(board, action))[0])
        if v > vMax[0]:
            vMax = (v, action)

    
    return vMax

def minValue(board):
    v = math.inf
    vMin = (v, ())
    if terminal(board):
        return (utility(board), None)
        #return utility(board)
    for action in actions(board):
        v = min(v, maxValue(result(board, action))[0])
        if v < vMin[0]:
             vMin = (v, action)

    return vMin

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        return maxValue(board)[1]
    elif player(board) == O:
        return minValue(board)[1]
    else:
        return None
