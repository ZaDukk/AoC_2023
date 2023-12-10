from collections import deque

def replace_character_at_index(input_string, index, new_char):
    string_list = list(input_string)
    string_list[index] = new_char
    return ''.join(string_list)

def add_box_around_grid(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])

   #top
    grid.insert(0, "+" * (num_cols + 2))

    #bottom
    grid.append("+" * (num_cols + 2))

    #sides
    for i in range(1, num_rows + 1):

        grid[i] = "+" + grid[i] + "+"

    return grid



with open("input.txt","r") as f:
    grid = [line.strip() for line in f.readlines()]


sRow =-1
sCol =-1

totalDots=0
for r,line in enumerate(grid):
    if "S" in line:
        sRow=r
        sCol = line.index("S")
    totalDots+=line.count(".")



# F7
# LJ

goesUp = "|LJ"
goesDown = "7F|"
goesRight = "LF-"
goesLeft = "-7J"

q = deque()

q.append(("7",sRow,sCol))
seen = set()
while q:
    current,r,c = q.popleft()
    if (r,c) in seen:
        continue
    seen.add((r,c))
    if current in goesUp and r>0 and grid[r-1][c] in goesDown:
        q.append((grid[r-1][c],r-1,c))
    if current in goesDown and r<len(grid) and grid[r+1][c] in goesUp:
        q.append((grid[r + 1][c], r + 1, c))
    if current in goesRight and c<len(grid[0]) and grid[r][c+1] in goesLeft:
        q.append((grid[r][c+1],r,c+1))
    if current in goesLeft and c>0 and grid[r][c-1] in goesRight:
        q.append((grid[r][c-1],r,c-1))

print(len(seen)//2)


Grid = []

for line in grid:
    Grid.append("*".join(line))
    Grid.append("*"*(len(grid[0])*2 -1))


Grid.pop()
grid = Grid

for line in grid:
    print(line)

for r,line in enumerate(grid):
    for c, current in enumerate(line):
        if r%2 ==0:
            if current =="*" and grid[r][c-1] in goesRight and grid[r][c+1] in goesLeft:
                grid[r] = replace_character_at_index(grid[r], c, "-")
        else:
            if current =="*" and grid[r+1][c] in goesUp and grid[r-1][c]in goesDown:
                grid[r] = replace_character_at_index(grid[r], c, "|")


grid = add_box_around_grid(grid)


grid[sRow] = replace_character_at_index(grid[sRow],sCol,"7")

q = deque()
dotsFound = 0
q.append((0,0))
seen = set()
vectors = [(0,1),(1,0),(-1,0),(0,-1)]
while q:
    r,c = q.popleft()
    if (r,c) in seen:
        continue
    if grid[r][c]==".":
        dotsFound+=1
    seen.add((r,c))
    for dr,dc in vectors:
        nr,nc = r+dr,c+dc
        if nr<0 or nr>= len(grid) or nc<0 or nc>=len(grid[0]):
            continue
        if grid[nr][nc] not in ".*+":
            continue
        q.append((nr,nc))

print(totalDots-dotsFound)



