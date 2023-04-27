#!/usr/bin/python3
"""
0. Lockboxes
"""


def canUnlockAll(boxes):
    """Write a method that determines if all the `boxes` can be opened.
    """
    keys = []  # a set that contains the keys found
    keys.extend(boxes[0])  # the first box is always open

    can_open = []
    for key, box in enumerate(boxes):

        if key == 0:
            can_open.append(True)
            continue
        else:
            # print(key, keys, box)
            if key in keys:
                can_open.append(True)
                keys.extend(box)
            else:
                can_open.append(False)
    # print(keys)
    return False if False in can_open else True
