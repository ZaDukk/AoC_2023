
from copy import deepcopy
from itertools import count
with open("input.txt","r") as f:
    grid = [list(line.strip()) for line in f.readlines()]


vector = (1,0)


for r,row in enumerate(grid):
    for c,cell in enumerate(row):
        if cell =="O":
            nr = r
            while nr > 0:
                if grid[nr-1][c] ==".":
                    grid[nr][c]  = "."
                    grid[nr-1][c]  ="O"
                elif grid[nr-1][c] in "O#":
                    break
                nr-=1
                if nr==0:
                    break








k = len(grid)
t=0
for line in grid:
    print(line)

for r,row in enumerate(grid):
    for c,cell in enumerate(row):
        if cell =="O":
            t+=k-r
print(t)


def rotate90Right(grid):
    rotated = zip(*grid[::-1])
    return rotated


def tiltNorth(Grid):
    grid = deepcopy(Grid)

    for r,row in enumerate(grid):
        for c,cell in enumerate(row):
            if cell =="O":
                nr = r
                while nr > 0:
                    if grid[nr-1][c] ==".":
                        grid[nr][c]  = "."
                        grid[nr-1][c]  ="O"
                    elif grid[nr-1][c] in "O#":
                        break
                    nr-=1
                    if nr==0:
                        break
    return grid

def cycle(Grid):
    grid = deepcopy(Grid)
    grid = rotate90Right(tiltNorth(rotate90Right(tiltNorth(rotate90Right(tiltNorth(rotate90Right(tiltNorth(grid))))))))
    return grid

def grid_to_tuple(grid):
    return tuple(tuple(row) for row in grid)

seen = {}

def weight(grid):
    t=0
    k = len(grid)
    for r,row in enumerate(grid):
        for c,cell in enumerate(row):
            if cell =="O":
                t+=k-r
    return t



for i in count(1):
    grid = cycle(grid)
    hashable = grid_to_tuple(grid)
    if hashable in seen:
        c = i - seen[hashable][0]
        #next two lines are somewhat coppied from reddit as i thought it was more elegant than my orignal soloution of storing an array of the hashables to get the offset alongside the dict
        for a, b in seen.values():
            if a >= seen[hashable][0] and a % c == 1_000_000 % c:
                print(b)
    seen[hashable] = (i,weight(grid))


