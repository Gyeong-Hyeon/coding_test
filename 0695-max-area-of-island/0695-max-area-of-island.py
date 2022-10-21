class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        def trav(vr, vc):
            if vr < 0 or vc < 0 or vr == len(grid) or vc == len(grid[0]) or grid[vr][vc] == 0:
                return 0
            grid[vr][vc] = 0
            return 1 + trav(vr-1, vc) + trav(vr+1, vc) + trav(vr, vc-1) + trav(vr, vc+1)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    ans = max(ans, trav(r,c))
        return ans