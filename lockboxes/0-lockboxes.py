#!/usr/bin/python3
"""
Module that determines if all lockboxes can be unlocked.
Contains the canUnlockAll function.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list): List of lists containing keys

    Returns:
        bool: True if all boxes can be opened, False otherwise
    """
    if not boxes or len(boxes) == 0:
        return False

    n = len(boxes)
    opened = {0}
    keys = set(boxes[0])

    while keys:
        key = keys.pop()

        if key < n and key not in opened:
            opened.add(key)
            keys.update(boxes[key])

    return len(opened) == n
