#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place.
    """
    if type(matrix) == list and len(matrix) > 0 and all(
            map(lambda x: type(x) == list, matrix)):
        rotated = [list(l[::-1]) for l in zip(*matrix)]
        for idx, i in enumerate(rotated):
            matrix[idx] = i
    else:
        return
