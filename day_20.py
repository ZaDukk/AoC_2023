from template import *
from math import lcm
from collections import deque,defaultdict


class flipFlop:
    def __init__(self,name,conected):
        self.conected = conected
        self.on = 0
        self.name = name

class conjuction:
    def __init__(self,name,conected):
        self.conected = conected
        self.memory = 0
        self.name = name
        self.into = {}
class broadcaster:
    def __init__(self,conected):
        self.conected = conected
        self.name = "broadcaster"

with open("input.txt","r") as f:
    inp = [line.strip() for line in f.readlines()]

q= deque()
modules  = []
start = broadcaster([])
for line in inp:
    module,conections = line.split(" -> ")[0],line.split(" -> ")[1]

    conections = conections.split(", ")
    moduleType,moduleName = module[0],module[1:]
    if moduleType == "b":
        start  =(broadcaster(conections))
    elif moduleType == "%":
        modules.append(flipFlop(moduleName,conections))
    else:
        modules.append(conjuction(moduleName,conections))

map = {}

for module in modules:
    map[module.name] = module



for module in modules:
    for neighbour in module.conected:
        if neighbour not in map:
            continue
        if type(map[neighbour]) == conjuction:
            map[neighbour].into[module.name] = 0


toSee = []
for module in modules:
    if "gf" in module.conected:
        toSee.append(module)

cycles = {}


step =0


lo =1
hi =0
while True:
    step+=1
    q = deque()
    q.append((start,0))

    while q:
        current,pulse = q.popleft()
        #print(pulse, current.name, type(current))
        if pulse:
            hi+=1
        else:
            lo+=1

        if type(current)==broadcaster:
            conected = current.conected


            for module in conected:
                q.append((map[module],0))
            continue

        if type(current)==flipFlop:
            if pulse: #high pulse
                continue
            #low pulse
            newState = not current.on

            for module in current.conected:
                if module not in map:
                    continue
                q.append((map[module],newState))
                if type(map[module]) == conjuction:
                    map[module].into[current] = newState



        if type(current)==conjuction:
            pulsesGoingIn = []
            pulseToSend = 1
            for i in current.into.values():
                pulsesGoingIn.append(i)
            if all(pulsesGoingIn):
                pulseToSend = 0

            for module in current.conected:
                if module not in map:
                    continue

                if module =="gf" and pulseToSend==1 and current in toSee:
                    toSee.remove(current)
                    cycles[current] = step


                if len(toSee)==0:
                    res=1
                    for cycle in cycles.values():
                        res = lcm(res,cycle)
                    print(res)
                    exit()




                q.append((map[module],pulseToSend))
                if type(map[module]) == conjuction:
                    map[module].into[current] = pulseToSend
    if step == 1000:
        print(lo*hi)









