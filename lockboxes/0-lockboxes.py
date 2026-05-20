#!/usr/bin/python3


def canUnlockAll(boxes):
    if not boxes or len(boxes) == 0:
        return False

    n = len(boxes)
    opened = {0}
    keys = list(boxes[0])

    while keys:
        key = keys.pop(0)

        if key < n and key not in opened:
            opened.add(key)
            keys.extend(boxes[key])

    return len(opened) == n
