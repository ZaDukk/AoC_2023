from collections import defaultdict,deque
from template import *

def bfsPart1(start,numOfSteps):
    q = deque()
    q.append((start,0))
    t=0
    seen=set()
    while q:
        (r,c),step = q.popleft()
        if (r,c,step) in seen:
            continue
        if step==numOfSteps:
            t+=1
            seen.add((r,c,step))
            continue
        if (r, c, step) in seen:
            continue
        seen.add((r, c, step))
        if step == numOfSteps + 1:
            break

        for dr,dc in vectors:
            nr,nc = r+dr,c+dc
            if nr<0 or nr>=len(inp) or nc<0 or nc>=len(inp[0]):
                if nr<0: nr = len(inp) - 1
                if nr>len(inp): nr = 0

                continue
            if inp[nr][nc]== "#":
                continue
            q.append(((nr,nc),step+1))

    return t
def findPossibleTiles(grid, start, steps):
    visited = defaultdict(set)
    visited[0].add(start)
    prevLen = 0
    history = []

    for s in range(steps):
        for point in visited[s]:
            r, c = point
            for dr,dc in vectors:
                nr, nc = r + dr, c + dc
                if grid.get((nr % width, nc % height), None) in ['.', 'S']:
                    visited[s + 1].add((nr, nc))

        if s % width == steps % width:
            prevLen = len(visited.get(s))
            history.append(prevLen)

        if len(history) == 3:
            break

    return history


def interpolateAndCalculateTiles(history, steps, width):
    #find coeficents 
    c = history[0]
    b = history[1] - history[0]
    a = history[2] - history[1]

    # interpolate using our quadratic
    return c + b * (steps // width) + (steps // width * (steps // width - 1) // 2) * (a - b)


with open("input.txt", "r") as f:
    inp = [line.strip() for line in f.readlines()]

grid = {}
start = None
width = len(inp[0])
height = len(inp)

for r, row in enumerate(inp):
    for c, cell in enumerate(row):
        grid[(r, c)] = cell
        if cell == 'S':
            start = (r, c)

p1 = bfsPart1(start,64)
print(f"P1: {p1}")
history = findPossibleTiles(grid, start, 26501365)
p2 = interpolateAndCalculateTiles(history, 26501365, width)
print(f"P2: {p2}")
