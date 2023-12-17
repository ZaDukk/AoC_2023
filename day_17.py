import heapq

grid = [list(map(int, line.strip())) for line in open("test.txt")]





def dijkstras(MINSTEPS,MAXSTEPS):
    vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = (0,0,0,0,0,0) #r,c,w,dr,dc,s
    goal = (len(grid)-1,len(grid[0])-1)

    q = [start]
    visited = set()
    while q:
        r,c,w,ddr,ddc,s = heapq.heappop(q)
        # print()

        if (r,c) == goal and s>=MINSTEPS:
            print(w)
            exit()

        if (r, c, ddr, ddc, s) in visited:
            continue
        visited.add((r, c, ddr, ddc, s))

        for dr,dc in vectors:
            nr,nc = r+dr,c+dc
            if nr <0 or nr >= len(grid) or nc <0 or nc >= len(grid[0]):
                continue


            newWeight = grid[nr][nc]

            if ddr == dr and ddc ==dc and s >= MAXSTEPS:
                continue
            if ddr == dr and ddc ==dc and s>MINSTEPS:
                heapq.heappush(q,(nr,nc,w+newWeight,ddr,ddc,s+1))
                continue

            if ddr == -dr and ddc == -dc:
                continue
            if s>=MINSTEPS:
                heapq.heappush(q,(nr,nc,w+newWeight,dr,dc,1))

print(dijkstras(1,3))
print(dijkstras(4,10))


