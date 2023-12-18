with open('input.txt', 'r') as f:
    inp = [line.strip() for line in f.readlines()]
def getDirectionsAndDistances(instruction, isPart2):
    if isPart2:
        instruction = instruction.split("#")[1].split(")")[0]
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)][int(instruction[-1])]
        distance = int(instruction[:-1], 16)
    else:
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)][['R', 'D', 'L', 'U'].index(instruction.split(" ")[0])]
        distance = int(instruction.split(" ")[1])
    return direction, distance

def calculateAreaAndPerimeter(inp, isPart2):
    position = (0, 0)
    points = [position]
    perimeter = 0

    for line in inp:
        direction, distance = getDirectionsAndDistances(line, isPart2)
        position = (position[0] + direction[0] * distance, position[1] + direction[1] * distance)
        perimeter += distance
        points.append(position)

    points = points[::-1]
    area = 0
    for i in range(len(points) - 1):
        area += (points[i][1] + points[i + 1][1]) * (points[i][0] - points[i + 1][0])

    return perimeter // 2 + area // 2 + 1


part1 = calculateAreaAndPerimeter(inp, False)
part2 = calculateAreaAndPerimeter(inp, True)
print(f"part1: {part1}")
print(f"part2: {part2}")


