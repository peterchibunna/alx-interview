#!/usr/bin/python3
"""
0. Lockboxes
"""


def canUnlockAll(boxes):
    """Write a method that determines if all the `boxes` can be opened.
    """
    keys = [0]  # a set that contains the keys found
    keys.extend(boxes[0])
    can_open = []
    unopened = []
    for key, box in enumerate(boxes):
        if key in keys:
            keys.extend(box)
            can_open.append(True)
        else:
            unopened.append({key: box})
            can_open.append(False)
    for d in unopened:
        for key in d:
            # if we are now able to open this box
            if key in keys:
                # replace the `cannot` status from the prior run
                # collect more keys from this box now and
                can_open.pop(key)
                keys.extend(d[key])
                can_open.insert(key, True)

    return False if False in can_open else True
