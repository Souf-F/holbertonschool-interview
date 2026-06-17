#!/usr/bin/python3

import sys


def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(board, row, n, solutions):
    if row == n:
        solution = [[i, board[i]] for i in range(n)]
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)


def nqueens(n):
    board = [-1] * n
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    return solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
