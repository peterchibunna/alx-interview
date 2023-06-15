#!/usr/bin/python3
"""
Module:
"""
from typing import List
import sys


def makeChange(coins: List, total: int) -> int:
    """Return fewer number of coins needed to meet `total`
    """
    if total <= 0:
        return 0
    m = len(coins)

    # table[i] will be storing the minimum
    # number of coins required for i value.
    # So table[total] will have result
    table = [0 for i in range(total + 1)]

    # Base case (If given value total is 0)
    table[0] = 0

    # Initialize all table values as Infinite
    for i in range(1, total + 1):
        table[i] = sys.maxsize

    # Compute minimum coins required
    # for all values from 1 to total
    for i in range(1, total + 1):

        # Go through all coins smaller than i
        for j in range(m):
            if coins[j] <= i:
                sub_res = table[i - coins[j]]
                if sub_res != sys.maxsize and sub_res + 1 < table[i]:
                    table[i] = sub_res + 1

    if table[total] == sys.maxsize:
        return -1

    return table[total]
