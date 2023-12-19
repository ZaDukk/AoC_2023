from collections import deque
from template import *

with open("input.txt", "r") as f:
    inp = f.read().strip()

rules, parts = inp.split('\n\n')

# Parse rules
R = {}
for rule in rules.split('\n'):
    name, rest = rule.split('{')
    R[name] = rest[:-1]
rules = R
# Parse parts
parsedParts = []
for partStr in parts.split('\n'):
    if partStr:
        partStr = partStr[1:-1]
        part = {x.split('=')[0]: int(x.split('=')[1]) for x in partStr.split(',')}
        parsedParts.append(part)

arr =[]
parts = parts.split("\n")
for part in parts:
    arr.append(extract_integers(part))
parts = arr


def isPartAccepted(part, name="in"):
    workFlow = rules[name].split(",")
    x, m, a, s = part


    for instruction in workFlow:
        if instruction == "R":
            return False
        if instruction == "A":
            return True
        if ":" not in instruction:
            return isPartAccepted(part, instruction)
        conditon = instruction.split(":")[0]
        if eval(conditon):
            if instruction.split(":")[1] == "R":
                return False
            if instruction.split(":")[1] == "A":
                return True
            return isPartAccepted(part, instruction.split(":")[1])



def adjustRange(operator, number, low, high):
    if operator == '>':
        low = max(low, number + 1)
    elif operator == '<':
        high = min(high, number - 1)
    elif operator == '>=':
        low = max(low, number)
    elif operator == '<=':
        high = min(high, number)
    else:
        assert False
    return (low, high)


def updateRanges(variable, operator, number, xLow, xHigh, mLow, mHigh, aLow, aHigh, sLow, sHigh):
    if variable == 'x':
        xLow, xHigh = adjustRange(operator, number, xLow, xHigh)
    elif variable == 'm':
        mLow, mHigh = adjustRange(operator, number, mLow, mHigh)
    elif variable == 'a':
        aLow, aHigh = adjustRange(operator, number, aLow, aHigh)
    elif variable == 's':
        sLow, sHigh = adjustRange(operator, number, sLow, sHigh)
    return (xLow, xHigh, mLow, mHigh, aLow, aHigh, sLow, sHigh)



def countAcceptedCombinations(rules):
    ans = 0
    initialRanges = (1, 4000, 1, 4000, 1, 4000, 1, 4000)
    Q = deque([('in', *initialRanges)])

    while Q:
        state, xLow, xHigh, mLow, mHigh, aLow, aHigh, sLow, sHigh = Q.pop()

        # Skip invalid states
        if xLow > xHigh or mLow > mHigh or aLow > aHigh or sLow > sHigh:
            continue

        if state == 'A':
            # Calculate and accumulate the score for accepted state
            score = (xHigh - xLow + 1) * (mHigh - mLow + 1) * (aHigh - aLow + 1) * (sHigh - sLow + 1)
            ans += score
        elif state == 'R':
            continue
        else:
            # Process rules for the current state
            rule = rules[state]
            for command in rule.split(','):
                condition, result = command.split(':') if ':' in command else (None, command)
                if condition:
                    variable, operator, number = condition[0], condition[1], int(condition[2:])
                    # Add next state and update ranges based on the rule
                    Q.append((result,
                              *updateRanges(variable, operator, number, xLow, xHigh, mLow, mHigh, aLow, aHigh, sLow,
                                            sHigh)))
                    # Adjust ranges for the inverse condition
                    xLow, xHigh, mLow, mHigh, aLow, aHigh, sLow, sHigh = updateRanges(
                        variable, '<=' if operator == '>' else '>=', number, xLow, xHigh, mLow, mHigh, aLow, aHigh,
                        sLow, sHigh
                    )
                else:
                    # Add next state without condition
                    Q.append((result, xLow, xHigh, mLow, mHigh, aLow, aHigh, sLow, sHigh))
                    break

    return ans

p1=0
for part in parts:
    if isPartAccepted(part):
        p1+=sum(part)
print(f"P1: {p1}")
p2 = countAcceptedCombinations(rules)
print(f"P2: {p2}")
