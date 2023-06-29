#!/usr/bin/python3
"""Module: 0. Prime Game
"""


def isWinner(x, nums):
    """Find out who the winner of the prime game is
    """
    if not nums or x < 1:
        return None
    n = max(nums)
    _filter = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not _filter[i]:
            continue
        for j in range(i * i, n + 1, i):
            _filter[j] = False
    _filter[0] = _filter[1] = False
    c = 0
    for i in range(len(_filter)):
        if _filter[i]:
            c += 1
        _filter[i] = c
    plyr1 = 0
    for n in nums:
        plyr1 += _filter[n] % 2 == 1
    if plyr1 * 2 == len(nums):
        return None
    if plyr1 * 2 > len(nums):
        return "Maria"
    return "Ben"
