class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix), len(matrix[0])
        start, end = [0,0], [m-1,n-1]
        while start <= end:
            l = (n-start[1] + (end[0]-start[0]-1)*n + end[1])//2
            mid = [start[0],start[1]+l]
            while mid[1] >= n:
                mid[0]+=1
                mid[1]-=n
            if matrix[mid[0]][mid[1]] == target:
                return True
            elif matrix[mid[0]][mid[1]] < target:
                if mid[1]+1 < n:
                    start = [mid[0],mid[1]+1]
                    continue
                else:
                    start = [mid[0]+1,0]
                    continue
            else:
                if mid[1]-1 >= 0:
                    end = [mid[0],mid[1]-1]
                    continue
                else:
                    end = [mid[0]-1,n-1]
        return False