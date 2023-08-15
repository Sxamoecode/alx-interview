#!/usr/bin/python3
"""
0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotating a 2D square matrix 90 degrees
    Args: matrix (list): 2d square
    Return: None
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        for j in range(int(n / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = temp
