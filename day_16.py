from collections import deque
with open("input.txt","r") as f:
    grid = [line.strip() for line in f.readlines()]


dirs = {"up":(-1,0),"down":(1,0),"left":(0,-1),"right":(0,1)}



def beam(start,direction):
    q = deque()
    seenStates = set()
    q.append(((start), (direction)))
    energized = set()
    counter =0

    while q:
        (r,c),(dr,dc)=q.popleft()
        if (r,c,dr,dc) in seenStates:
            continue
        seenStates.add((r,c,dr,dc))

        if (r,c) not in energized:
            energized.add((r,c))
        nr,nc = r+dr,c+dc

        if nr<0 or nr>=len(grid) or nc<0 or nc>=len(grid[0]):
            continue

        if grid[nr][nc]==".":
            q.append(((nr,nc),(dr,dc)))
            continue

        if grid[nr][nc]=='\\':
            if (dr,dc) ==dirs["right"]:
                q.append(((nr,nc),dirs["down"]))
                continue

            if (dr,dc) ==dirs["left"]:
                q.append(((nr,nc),dirs["up"]))
                continue

            if (dr,dc) == dirs["up"]:
                q.append(((nr,nc),dirs["left"]))
            if (dr,dc) == dirs["down"]:
                q.append(((nr,nc),dirs["right"]))
            continue

        if grid[nr][nc]=="/":
            if (dr,dc) ==dirs["right"]:
                q.append(((nr,nc),dirs["up"]))
                continue
            if (dr,dc) ==dirs["left"]:
                q.append(((nr,nc),dirs["down"]))
                continue
            if (dr,dc) == dirs["up"]:
                q.append(((nr,nc),dirs["right"]))
                continue
            if (dr,dc) == dirs["down"]:
                q.append(((nr,nc),dirs["left"]))
                continue
            print("something has gone wrong")
            exit()

        if grid[nr][nc]=="-":
            if (dr,dc) ==dirs["left"] or (dr,dc) == dirs["right"]:
                q.append(((nr,nc),(dr,dc)))
            if (dr,dc) == dirs["up"] or (dr,dc) == dirs["down"]:
                q.append(((nr,nc),dirs["left"]))
                q.append(((nr,nc),dirs["right"]))

        if grid[nr][nc]=="|":
            if (dr,dc) ==dirs["up"] or (dr,dc) == dirs["down"]:
                q.append(((nr,nc),(dr,dc)))
            if (dr,dc) == dirs["left"] or (dr,dc) == dirs["right"]:
                q.append(((nr,nc),dirs["up"]))
                q.append(((nr,nc),dirs["down"]))
        counter+=1

    return (len(energized) - 1)


print(f"p1: {beam((0, -1), (0, 1))}")
nums = [beam((-1,i),(1,0)) for i in range(len(grid[0]))]
print(f"p2: {max(nums)}")