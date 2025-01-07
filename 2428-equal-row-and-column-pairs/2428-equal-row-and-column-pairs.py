class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols, ans = {}, 0
        for i in range(len(grid)):
            li = []
            for j in range(len(grid)):
                li.append(grid[j][i])
            li = tuple(li)
            cols[li] = cols.get(li,0) + 1
        
        for row in grid:
            ans = ans + cols.get(tuple(row),0)
        return ans