
N = 8


def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True
def solve_n_queens(board, row=0):
    if row == N:
        print_solution(board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if solve_n_queens(board, row + 1):
                return True
            board[row] = -1  
    return False
def print_solution(board):
    for row in range(N):
        line = ['Q' if board[row] == col else '.' for col in range(N)]
        print(' '.join(line))
    print()
board = [-1] * N
solve_n_queens(board)
