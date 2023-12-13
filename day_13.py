with open("input.txt","r") as f:
    inp = [line.strip() for line in f.readlines()]


def validIndexes(a,b,lim):
    return 0<a<b<lim

def horizontal(grid,smudges=0):
    for i, line in enumerate(grid):
        if i + 1 == len(grid):
            return 0
        pairs = []

        for line1, line2 in zip(grid[i::-1], grid[i + 1:]):

            for c1, c2 in zip(line1, line2):
                pairs.append((c1, c2))

        matches = sum(1 for c1, c2 in pairs if c1 == c2)

        if matches == len(pairs) - smudges:
            return i + 1

def vertical(grid, smudges=0):
    #transpose the grid
    return horizontal(list(zip(*grid)), smudges)

grids = []
current = []
for line in inp:
    if len(line)!=0:
        current.append(line)
        continue
    grids.append(current)
    current=[]
else:
    grids.append(current)
p1=0
p2=0
for grid in grids:
    p1+=100*horizontal(grid) + vertical(grid)
    p2+=100*horizontal(grid,1) + vertical(grid,1)
print(f"p1: {p1}")
print(f"p2: {p2}")


