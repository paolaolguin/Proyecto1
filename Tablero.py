#Funcion que imprime tablero

board = []

for row in range(10):
    board.append([])
    for column in range(10):
        board[row].append('0')

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

