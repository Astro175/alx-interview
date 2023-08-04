#!/usr/bin/python3

"""Module that uses DFS for lockboxes"""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists representing
        the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True

    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
