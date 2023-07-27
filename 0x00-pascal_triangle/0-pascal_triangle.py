#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """
    function def pascal_triangle(n): that returns a list of lists of integers
                                     representing the Pascal’s triangle of n:
    Returns an empty list if n <= 0
    You can assume n will be always an integer
    """
    if n <= 0:
        return []

    pascal = [[1]]
    for i in range(1, n):
        row = [1]
        prev = pascal[i - 1]
        for j in range(len(prev)):
            new = prev[j] + prev[j + 1] if j != len(prev) - 1 else 1
            row.append(new)

        pascal.append(row)

    return pascal
