class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        1. Find the cells with value of 2 and insert the cell's position into a queue.
        2. Count the number of cells with value of 1
        3-1. If there is no cells with value of 1, return 0
        3-2. If there is cells with value of 1 but no cells with value of 2, return -1
        4. Take one by one from queue and check if there is any 4 directionally adjacent cells with value of 1
            - If yes, change's value to 2, put the cell's position into the queue, and count it
            - Once the first group's queue is empty, sec+1            
        3. If counts 4 and counts 2 is same, return sec-1 (sec counted +1 in the loop because the last cell with value of two was in the queue). Else, return -1
        """
        if not grid:
            return -1
        q = []
        is_one = 0
        #find where 2 is & count the number of 1
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

        sec=0
        DIR = [-1, 0, 1, 0, -1] #table to check the 4 directionally adjacent cells
        while q:
            sec+=1
            for _ in range(len(q)):
                r, c = q.pop(0)
                for i in range(4): 
                    fr, fc = r+DIR[i], c+DIR[i+1]
                    if fr < 0 or fc < 0 or fr == len(grid) or fc == len(grid[0]) or grid[fr][fc] != 1:
                        continue
                    grid[fr][fc] = 2
                    q.append((fr,fc))
                    is_one-=1
        if not is_one:
            return sec-1 #-1 for the last cell
        else:
            return -1             