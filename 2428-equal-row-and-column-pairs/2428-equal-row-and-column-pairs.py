class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        reversed_grid = [[grid[y][x] for y in range(len(grid))] for x in range(len(grid[0]))]
        answer = 0
        for row in grid:
            answer+=reversed_grid.count(row)
        return answer