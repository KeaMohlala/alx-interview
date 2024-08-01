#!/usr/bin/python3
""" module to document the lockboxes function"""


def canUnlockAll(boxes):
    """
    method to determine if all boxes can be opened
    Args: boxes - a list of lists
    Return: true if all boxes can be opened else return false
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    current_box_keys = boxes[0]

    while current_box_keys:
        key = current_box_keys.pop()
        if key < n and not unlocked[key]:
            # mark as unlocked
            unlocked[key] = True
            # add keys from this box
            current_box_keys.extend(boxes[key])

    # Check if all boxes are unlocked
    return all(unlocked)
