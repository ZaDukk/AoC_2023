with open("input.txt","r") as f:
    grid = [line.strip() for line in f.readlines()]
def is_character_in_column(grid, column_index, target_character):
    for row in grid:
        if row[column_index] == target_character:
            return True
    return False


silentRows = [r for r,row in enumerate(grid) if not "#" in row]
silentCols = [c for c in range(len(grid[0])) if not is_character_in_column(grid,c,"#")]


galaxies = []
for r,row in enumerate(grid):
    for c,current in enumerate(row):
        if current=="#":
            galaxies.append((r,c))

pairs = [(galaxies[i], galaxies[j]) for i in range(len(galaxies)) for j in range(i + 1, len(galaxies))]
part1 =0
part2=0


for pair in pairs:
    (r1,c1),(r2,c2) = pair
    part1 += abs(r1 - r2) + abs(c1 - c2)
    part2 += abs(r1 - r2) + abs(c1 - c2)
    for row in silentRows:
        if min(r1,r2) < row < max(r1,r2):
            part1+=1
            part2+=99999
    for col in silentCols:
        if min(c1,c2) < col < max(c1,c2):
            part1+=1
            part2+=99999
print(part1)
print(part2)






