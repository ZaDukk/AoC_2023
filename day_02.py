with open("input.txt","r") as f:
    inp = [line.strip() for line in f.readlines()]

#part1
res=0
gameNum = 0
for line in inp:
    gameNum+=1
    thisGameWorks = True
    rounds = line.split(": ")[1].split("; ")
    for round in rounds:
        dict = {"red":0, "green":0,"blue":0}
        cubes = round.split(", ")
        for cube in cubes:
            numColour = cube.split()
            dict[numColour[1]] = int(numColour[0])

        if (dict["red"]>12 or dict["green"]>14 or dict["blue"]>15):
            thisGameWorks=False
            break
    if thisGameWorks:
        res+=gameNum
print(res)

#part2
res=0
for line in inp:
    gameNum+=1
    rounds = line.split(": ")[1].split("; ")
    dict = {"red": 0, "green": 0, "blue": 0}
    for round in rounds:
        cubes = round.split(", ")
        for cube in cubes:
            numColour = cube.split()
            dict[numColour[1]] = max(int(numColour[0]), dict[numColour[1]])
    res+=dict["red"]*dict["green"]*dict["blue"]
print(res)
