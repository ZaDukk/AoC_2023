from time import process_time
from collections import defaultdict
from template import *

#I used the wrong account when submitting my answers so on my main account it looks like i have an 11 second delta time!
#unforunetly i am not actually that fast :(

def buildEdges(grid):
    edges = defaultdict(set)
    for r, row in enumerate(grid):
        for c, v in enumerate(row):
            if v == ".":
                for dr, dc in vectors:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(row) and grid[nr][nc] == ".":
                        edges[(r, c)].add((nr, nc))
                        edges[(nr, nc)].add((r, c))
            elif v == ">":
                edges[(r, c)].add((r, c + 1))
                edges[(r, c - 1)].add((r, c))
            elif v == "v":
                edges[(r, c)].add((r + 1, c))
                edges[(r - 1, c)].add((r, c))
    return edges

def findLongestPath(grid, edges):
    endPoint = (len(grid) - 1, len(grid[0]) - 2)
    startPoint = (0, 1, 0)
    q = [startPoint]
    visited = set()
    biggest = 0

    while q:
        r, c, l = q.pop()
        if l == -1:
            visited.remove((r, c))
            continue
        if (r, c) == endPoint:
            biggest = max(biggest, l)
            continue
        if (r, c) in visited:
            continue
        visited.add((r, c))
        q.append((r, c, -1))
        for ar, ac in edges[(r, c)]:
            q.append((ar, ac, l + 1))

    return biggest

# Part 2
def buildEdgesPart2(grid):
    edges = defaultdict(set)
    for r, row in enumerate(grid):
        for c, v in enumerate(row):
            if v in ".>v":
                for dr, dc in vectors:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(row) and grid[nr][nc] in ".>v":
                        edges[(r, c)].add((nr, nc, 1))
                        edges[(nr, nc)].add((r, c, 1))
    return edges

def mergeEdges(edges):
    while True:
        for current, conected in edges.items():
            if len(conected) == 2:
                a, b = conected
                edges[a[:2]].remove(current + (a[2],))
                edges[b[:2]].remove(current + (b[2],))
                edges[a[:2]].add((b[0], b[1], a[2] + b[2]))
                edges[b[:2]].add((a[0], a[1], a[2] + b[2]))
                del edges[current]
                break
        else:
            break

def findLongestPathPart2(grid, edges):
    endPoint = (len(grid) - 1,len(grid[0])-2)
    startPoint = (0, 1, 0)
    q = [startPoint]
    visited = set()
    best = 0

    while q:
        r, c, l = q.pop()
        if l == -1:
            visited.remove((r, c))
            continue
        if (r, c) == endPoint:
            best = max(best, l)
            continue
        if (r, c) in visited:
            continue
        visited.add((r, c))
        q.append((r, c, -1))
        for nr, nc, l in edges[(r, c)]:
            q.append((nr, nc, l + l))

    return best

#main
startTime = process_time()
with open("input.txt", "r") as f:
    grid = [line.strip() for line in f.readlines()]

part1 = findLongestPath(grid, buildEdges(grid))
print(f"P1: {part1}")


edgesPart2 = buildEdgesPart2(grid)
mergeEdges(edgesPart2)
part2 = findLongestPathPart2(grid, edgesPart2)
print(f"P2: {part2}")



print(process_time() - startTime)
