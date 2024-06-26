class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, cnt = len(matrix)-1, len(matrix)//2
        for i in range(cnt+1):
            for j in range(i, n-i):
                matrix[j][n-i], matrix[n-i][n-j], matrix[n-j][i], matrix[i][j] = matrix[i][j], matrix[j][n-i], matrix[n-i][n-j], matrix[n-j][i]