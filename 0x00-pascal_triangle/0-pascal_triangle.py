#!/usr/bin/python3
"""0. Pascal's triangle
"""


def pascal_triangle(n):
    """
    return a list of integers representing Pascal's triangle of size n
    :param n:
    :return:
    """
    if n <= 0 or type(n) is not int:
        return []
    rows = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if i == j or j == 0:
                # if we are at the beginning or end of the row
                row.append(1)
            else:
                # in the nth row, add the nth item of the previous row
                # to the nth+1 item of the same previous row
                row.append(rows[i - 1][j - 1] + rows[i - 1][j])
        rows.append(row)

    return rows
