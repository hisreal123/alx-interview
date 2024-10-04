#!/usr/bin/env python3
#  a list of lists of integers representing the pascal's triangle of n;

def pascal_triangle(n):
    triangle = [[1]]  # First row is always [1]

    """ a function that returns a list of lists of integers representing n"""
    if n <= 0:
        return []

    for i in range(1, n):
        row = [1]  # Start each row with 1 and there about

        # Build the middle elements of the row and there about
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
