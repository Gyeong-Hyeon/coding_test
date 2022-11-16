class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        1. Define a function check_island(r,c):
            - if there is no island on left, up, down, right, or current island is 0:
                return 0
            - else, change current island to 0 to avoid double check (we don't need to check if current island is 1 because the value is either 0 or 1 and we already checked it's not 0)
            - return 1(the current island's width)
                + check_island(r-1,c) #check the island connected at downside recursively
                + check_island(r+1,c) #check the island connected at upside recursively
                + check_island(r,c-1) #check the island connected at left side recursively
                + check_island(r,c+1) #check the island connected at right side recursively
            ==> Final return value will be total width of island connect with start point
        2. Set a initial max_w to 0 and start to rotate Grid from grid[0][0]
            - if value == 0: pass
            - else: max_w = max(max_w, check_island(r,c))
        3. return max_len
        """
        def check_width(r,c):
            if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1+check_width(r-1,c)+check_width(r+1,c)+check_width(r,c-1)+check_width(r,c+1)
        max_w = 0
        for gr in range(len(grid)):
            for gc in range(len(grid[0])):
                if grid[gr][gc]:
                    max_w = max(max_w,check_width(gr,gc))
        return max_w