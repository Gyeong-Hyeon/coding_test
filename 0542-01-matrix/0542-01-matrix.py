class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        The cells connected 4 directionally from a cell with value 0 will have value of 1.
        The cells connected 4 directionally from the cells 4 directionally connected from a cell with value 0 will have value of 2.
        We can see that the value increases by 1 as cells away from the cell with 0 in 4 directions.
        Therefore,
        - Check where 0 is/are
        - Add up the values current cell's value+1 by checking the cells in 4 directions
        - We should check the cells in order of a value
        - visit list is needed to avoid adding 1 to a duplicated cell
        """
        q = []
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    q.append((r,c))
                else:
                    mat[r][c] = -1 #to mark it's unvisited
        dt = [-1, 0, 1, 0, -1]
        while q:
            for _ in range(len(q)):
                r, c = q.pop(0)
                dist = mat[r][c]
                for i in range(4):
                    nr, nc = r+dt[i], c+dt[i+1]
                    if nr < 0 or nc < 0 or nr == len(mat) or nc == len(mat[0]) or mat[nr][nc] > -1:
                        continue
                    mat[nr][nc] = dist+1
                    q.append((nr,nc))
        return mat                    