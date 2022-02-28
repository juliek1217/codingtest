# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # swap column and row
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                # swap1 = matrix[i][j]
                # swap2 = matrix[j][i]
                # matrix[i][j] = swap2
                # matrix[j][i] = swap1
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reverse rows
        for i in range(len(matrix)):
            matrix[i].reverse()
