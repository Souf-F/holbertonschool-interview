#!/usr/bin/python3
"""
the N Queen program
"""
import sys


def create_board(n):
    return []


def safe_square(row, col, board):
    for i, j in board:
        if j == col:
            return False
        if abs(i - row) == abs(j - col):
            return False
    return True


def backtracking(n, row, board, result):
    if row == n:
        result.append(list(board))
        return

    for col in range(n):
        if safe_square(row, col, board):
            board.append([row, col])
            backtracking(n, row + 1, board, result)
            board.pop()


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

    result = []
    board = create_board(n)
    backtracking(n, 0, board, result)

    for results in result:
        print(results)


if __name__ == "__main__":
    main()
