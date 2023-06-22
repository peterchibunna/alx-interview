#!/usr/bin/python3

"""
0x09. Island Perimeter
"""


def get_edges(grid: list, row: int, col: int) -> int:
    """get the edges of the island
    """
    sides = 0
    if grid[row][col] == 1:
        sides += is_water(grid, row, col - 1) + \
                 is_water(grid, row - 1, col) + \
                 is_water(grid, row, col + 1) + \
                 is_water(grid, row + 1, col)
    return sides


def is_water(grid: list, row: int, col: int) -> int:
    """return 0 if point is water, 1 if land
    """
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        if grid[row][col] == 1:
            return 0
    return 1


def island_perimeter(grid) -> int:
    """returns the perimeter of the island described in
    `grid`
    """

    if type(grid) == list:
        perimeter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                perimeter += get_edges(grid, row, col)
        return perimeter
    else:
        return 0
