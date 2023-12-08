from math import lcm

with open("input.txt","r") as f:
    inp = [line.strip() for line in f.readlines()]
instructions ="LLRLRLLRRLRLRLLRRLRRRLRRRLRRLRRLRLRLRRRLLRLRRLRLRRRLRLLRRLRLRLLRRRLLRLRRRLRLRRLRRLRLLRRLRRLRLRLRLLRLLRRLRRLRRLRRLRRLRLLRLRLRRRLRRRLRRLRLRLRRLRRRLRLRRRLRLRLRLRRRLRRLRRLRRRLLLLRRLRRLRLRRRLRLRRRLRRLLLLRLRLRRRLRRRLRLRRLLRLRLRRRLRLRLRRRLRLLRRRLRRLRLRLRRRLRLLRRLLRRRLRRRLRRRLRRLRLRLRRRLRRRLRRRLLRRRR"

nextPlaces = {}

for line in inp:
    x = line.split(" = ")
    nextPlaces[x[0].strip()] = x[1].strip()

current = "AAA"
steps =0
move = 0

while True:
    currentInstruction = instructions[move]
    if currentInstruction =="L":
        current=nextPlaces[current].split(", ")[0].strip("(")
    else:
        current = nextPlaces[current].split(", ")[1].strip(")")
    steps+=1
    if current=="ZZZ":
        print(f"p1: {steps}")
        break
    move= (move+1)%len(instructions)

steps =1


def stepsToZ(startNode):
    current = startNode
    steps = 0
    move = 0
    while True:
        currentInstruction = instructions[move]
        if currentInstruction == "L":
            current = nextPlaces[current].split(", ")[0].strip("(")
        else:
            current = nextPlaces[current].split(", ")[1].strip(")")
        steps += 1
        if current[-1]=="Z":
            return steps
        move = (move + 1) % len(instructions)


for node in nextPlaces.keys():
    if node[-1]=="A":
        steps = lcm(steps,stepsToZ(node))
print(f"p2: {steps}")







