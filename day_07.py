from functools import cmp_to_key

card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def getRank(hand):
    x=''.join(sorted(hand))
    if hand[0]*5 ==hand:
        return 7
    if x[0]*4 == x[:-1] or x[-1]*4 == x[1:]:
        return 6
    if (x[0]==x[1] ==x[2] and x[3]==x[4]) or (x[0]==x[1] and x[2]== x[3]==x[4]):
        return 5
    #three of a kind / two pair (stolen from #bannadado beacuse my orignal one was very ugly)
    if len(set(hand)) == 3:
        if any([hand.count(x) == 3 for x in set(hand)]):
            return 4
        else:
            #two of a kind
            return 3
    if (x[0]!=x[1]!=x[2]!=x[3]!=x[4]):
        return 1
    return 2

def cmp(handA,handB):
    if getRank(handA)!=getRank(handB):
        return getRank(handA)-getRank(handB)
    else:
        for i in zip(handA,handB):
            handACurrent,handBcurrent = i
            if card_values[handACurrent]!=card_values[handBcurrent]:
                return card_values[handACurrent]-card_values[handBcurrent]
    return 0

def cmp2(handA,handB):
    handARank=0
    handBRank =0
    for i in card_values.keys():
        handARank = max(handARank,getRank(handA.replace("J",i)))
        handBRank = max(handBRank,getRank(handB.replace("J",i)))
    if handARank!= handBRank:
        return handARank-handBRank
    else:
        for i in zip(handA,handB):
            handACurrent,handBcurrent = i
            if card_values[handACurrent]!=card_values[handBcurrent]:
                return card_values[handACurrent]-card_values[handBcurrent]
    return 0


#2332 -> #22333 -> #33322
with open("input.txt","r") as f:
    inp = [line.strip() for line in f.readlines()]


betValues = {}
hands = []

for line in inp:
    hand,bet = tuple(line.split())
    hands.append(hand)
    betValues[hand]=bet



s = 0
sortedHands = sorted(hands,key=cmp_to_key(cmp))
for i,x in enumerate(sortedHands):
    s+=int(i+1)*int(betValues[x])
print(s)

card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 0, 'Q': 12, 'K': 13, 'A': 14}

s = 0
sortedHands = sorted(hands,key=cmp_to_key(cmp2))
for i,x in enumerate(sortedHands):
    s+=int(i+1)*int(betValues[x])
print(s)
