class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        1. Find the cells with value of 2 and insert the cell's position into a queue.
        2. If any of the cells connected 4 directionally with the cells with value of 1's value is 1, change it's value to 2, cnt+1 and insert it's position into a queue.
            - Since oranges becomes rotten simultaneously, all cells in 4 direction corresponding to the above case are grouped together and put into a queue.
        3. count starts from -1 to return -1 if there was fresh orange but never rotten.
        """
        if not grid:
            return -1
        q = []
        is_one = 0
        #find where 2 is
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    continue
                if grid[r][c] == 2:
                    q.append((r,c))
                else:
                    is_one+=1
        if not is_one:
            return 0
        if not q:
            return -1
        
        is_rot=False
        sec=0
        DIR = [-1, 0, 1, 0, -1]
        while q:
            if is_rot:
                sec+=1
                is_rot=False
            for _ in range(len(q)):
                r, c = q.pop(0)
                for i in range(4):
                    fr, fc = r+DIR[i], c+DIR[i+1]
                    if fr < 0 or fc < 0 or fr == len(grid) or fc == len(grid[0]) or grid[fr][fc] != 1:
                        continue
                    grid[fr][fc] = 2
                    q.append((fr,fc))
                    is_one-=1
                    is_rot=True
        if not is_one:
            return sec
        else:
            return -1             