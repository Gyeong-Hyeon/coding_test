def orangesRotting(grid) -> int:
    if not grid:
        return -1
    rows = len(grid)
    cols = len(grid[0])
    to_visit=set()        
    def rot(r,c):
        cnt = 0
        if r-1 > 0:
            if grid[r-1][c] == 1:
                grid[r-1][c] = 2
                to_visit.add((r-1,c))
                cnt+=1
        if r+1 < rows:
            if grid[r+1][c] == 1:
                grid[r+1][c] = 2
                to_visit.add((r+1,c))
                cnt+=1
        if c-1 > 0:
            if grid[r][c-1] == 1:
                grid[r][c-1] = 2
                to_visit.add((r,c-1))
                cnt+=1
        if c+1 < cols:
            if grid[r][c+1] == 1:
                grid[r][c+1] = 2
                to_visit.add((r,c+1))
                cnt+=1
        return cnt
    m = 0
    for nr in range(rows):
        for nc in range(cols):
            if grid[nr][nc] == 2:
                cnt=rot(nr,nc)
                if cnt > 0:
                    m+=1                
    while to_visit:
        vr, vc = to_visit.pop()
        cnt=rot(vr,vc)
        if cnt > 0:
            m+=1
    return m
  
  if __name__ == "__main__":
    assert orangeRotting([[2,1,1],[0,1,1],[1,0,1]]) == 4 #-1
  
