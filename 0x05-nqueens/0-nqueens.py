#!/usr/bin/python3
"""
N Queens Problem Solver
"""
import sys


def print_solution(solution):
    """
    Prints the solution in the required format.
    Args:
        solution (list): The list of solutions (row, col) for each queen.
    """
    print([[i, solution[i]] for i in range(len(solution))])


def is_safe(solution, row, col):
    """
    Check if a queen can be placed at (row, col) without being attacked.
    Args:
        solution (list): The current state of the solution.
        row (int): The row where the queen is to be placed.
        col (int): The column where the queen is to be placed.
    Returns:
        bool: True if safe, False otherwise.
    """
    for i in range(row):
        if solution[i] == col or abs(solution[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(N, row, solution):
    """
    Solves the N Queens problem using backtracking.
    Args:
        N (int): The size of the chessboard (N x N).
        row (int): The current row being processed.
        solution (list): The current solution state.
    """
    if row == N:
        print_solution(solution)
    else:
        for col in range(N):
            if is_safe(solution, row, col):
                solution[row] = col
                solve_nqueens(N, row + 1, solution)


def nqueens(N):
    """
    Solves the N Queens problem for a board of size N.
    Args:
        N (int): The size of the chessboard (N x N).
    """
    solution = [-1] * N
    solve_nqueens(N, 0, solution)


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is a valid integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N Queens problem
    nqueens(N)
