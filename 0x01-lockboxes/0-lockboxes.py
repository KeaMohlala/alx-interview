#!/usr/bin/python3
""" module to document the lockboxes function"""


def canUnlockAll(boxes):
    """
    method to determine if all boxes can be opened
    Args: boxes - a list of lists
    Return: true if all boxes can be opened else return false
    """
    # Initialize a set to keep track of visited boxes
    visited_boxes = set()

    # Start from the first box (index 0)
    current_box_keys = boxes[0]

    while current_box_keys:
        # Mark the current box as visited
        visited_boxes.add(len(current_box_keys) - 1)

        # Update the current box keys with the keys found in the current box
        next_box_keys = []
        for key in current_box_keys:
            if key < len(boxes):
                next_box_keys.extend(boxes[key])

        # Move to the next box
        current_box_keys = next_box_keys

    # Check if all boxes were visited
    return len(visited_boxes) == len(boxes)
