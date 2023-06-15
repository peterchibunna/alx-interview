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
    change_todo = total
    moves = 0
    coin_idx = 0  # where in the coins list traversal are we at
    coins.sort(reverse=True)
    while change_todo > 0:
        if coin_idx >= len(coins):
            return -1
        if change_todo - coins[coin_idx] >= 0:
            change_todo -= coins[coin_idx]
            moves += 1
        else:
            coin_idx += 1
    return moves
