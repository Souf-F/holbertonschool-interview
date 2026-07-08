#!/usr/bin/python3
"""Module that calculates the perimeter of an island in a grid."""


def island_perimeter(grid):
    """Return the perimeter of the island described in grid.

    Args:
        grid (list of list of int): 2D grid where 0 is water and
            1 is land. The grid is rectangular and completely
            surrounded by water, with a single island and no lakes.

    Returns:
        int: the perimeter of the island.
    """
    perimeter = 0
    height = len(grid)

    for row in range(height):
        width = len(grid[row])
        for col in range(width):
            if grid[row][col] == 1:
                perimeter += 4
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
