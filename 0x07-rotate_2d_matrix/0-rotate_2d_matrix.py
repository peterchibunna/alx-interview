#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place.
    """
    # if type(matrix) != list:
    #     return
    # if len(matrix) <= 0:
    #     return
    # if not all(map(lambda x: type(x) == list, matrix)):
    #     return
    if type(matrix) == list and len(matrix) > 0 and all(
            map(lambda x: type(x) == list, matrix)):
        rows = len(matrix)
        columns = len(matrix[0])
        if not all(map(lambda x: len(x) == columns, matrix)):
            return
        cols, rws = 0, rows - 1
        for i in range(columns * rows):
            if i % rows == 0:
                matrix.append([])
            if rws == -1:
                rws = rows - 1
                cols += 1
            matrix[-1].append(matrix[rws][cols])
            if cols == columns - 1 and rws >= -1:
                matrix.pop(rws)
            rws -= 1
    else:
        return
