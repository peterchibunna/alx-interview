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
    remaining = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while remaining > 0:
        if coin_idx >= n:
            return -1
        if remaining - sorted_coins[coin_idx] >= 0:
            remaining -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
