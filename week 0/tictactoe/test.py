from tictactoe import winner, terminal, player, utility, maxValue, minValue, EMPTY, X, O, result, actions, minimax


def test_winner():
    """
    Test the winner function.
    """
    print(winner([['X', ' ', ' '], 
                   [' ', 'X', ' '], 
                   [' ', ' ', 'X']]))
    assert winner([['X', 'X', 'X'], 
                   ['O', 'O', 'X'], 
                   ['O', 'X', 'O']]) == 'X'
    assert winner([['O', 'O', 'O'], 
                   ['X', 'X', 'O'], 
                   ['X', 'O', 'X']]) == 'O'
    assert winner([['X', 'O', 'X'], 
                   ['O', 'X', 'O'], 
                   ['O', 'X', 'X']]) == 'X'
    assert winner([['O', 'X', 'O'], 
                   ['X', 'O', 'X'], 
                   ['X', 'O', 'O']]) == 'O'
    assert winner([[' ', ' ', ' '], 
                   [' ', ' ', ' '], 
                   [' ', ' ', ' ']]) == None
    assert winner([['X', ' ', ' '], 
                   [' ', 'X', ' '], 
                   [' ', ' ', 'X']]) == 'X'
    assert winner([['O', ' ', ' '], 
                   [' ', 'O', ' '], 
                   [' ', ' ', 'O']]) == 'O'
    assert winner([['X', ' ', 'O'], 
                   [' ', 'X', 'O'], 
                   ['O', ' ', 'X']]) == 'X'

# board =  [[X, O, X],
#           [X, X, O],
#           [O, X, O]]

board2 = [[X, O, X],
          [EMPTY, EMPTY, EMPTY],
          [EMPTY, EMPTY, O]]

board3 = [[X, X, O],
          [O, O, X],
          [X, O, X]]

print(actions(board3))



print(terminal(board3))
print(utility(board3))

#print(minValue(board2))
print(minimax(board3))

test_winner()