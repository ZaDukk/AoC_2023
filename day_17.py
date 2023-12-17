from heapq import heappush, heappop
from template import *

grid = [list(map(int, line.strip())) for line in open("input.txt","r")]

def dijkstras(MAXSTEPS,MINSTEPS):
    seen = set()
    q = [(0, 0, 0, 0, 0, 0)]
    goal = (len(grid)-1, len(grid[0])-1)

    while q:
        w, r, c, dr, dc, s = heappop(q)

        if goal == (r,c) and s>MINSTEPS:
            return (w)



        if (r, c, dr, dc, s) in seen:
            continue

        seen.add((r, c, dr, dc, s))

        if s < MAXSTEPS and (dr, dc) != (0, 0):
            nr,nc = r + dr,c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                heappush(q, (w + grid[nr][nc], nr, nc, dr, dc, s + 1))

        if s<MINSTEPS and (r,c)!=(0,0):#if its the start it is allowed
            continue

        for ddr, ddc in vectors:
            if (ddr, ddc) == (dr, dc) or (ddr, ddc) == (-dr, -dc):
                continue
            nr,nc= r + ddr,c + ddc
            if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                continue
            heappush(q, (w + grid[nr][nc], nr, nc, ddr, ddc, 1))



print(dijkstras(3,1))
print(dijkstras(10,4))