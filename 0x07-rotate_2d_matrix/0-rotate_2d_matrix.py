#!/usr/bin/python3
"""2D matrix rotation module.
"""


def myzip(*iterables):
    """Let me take a shot at implementing my own zip function so I can do
    away with the builtin zip method. Hahaha
    """
    new_list = []
    x = len(iterables)
    n = len(iterables[0])
    for i in range(n):
        new_item = tuple(iterable[i] for iterable in iterables)
        new_list.append(new_item)
    return new_list


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place.
    """
    if type(matrix) == list and len(matrix) > 0 and all(
            map(lambda x: type(x) == list, matrix)):
        rotated = [list(item[::-1]) for item in myzip(*matrix)]
        # this below, will allow us to overwrite an outside variable from this
        # inner scope
        for idx, i in enumerate(rotated):
            matrix[idx] = i
    else:
        return
