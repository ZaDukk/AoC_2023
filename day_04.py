from math import  floor
import re
from collections import  defaultdict
def extract_integers(input_string, allow_negative=False):
    pattern = r'-?\d+' if allow_negative else r'\d+'
    integers = re.findall(pattern, input_string)
    integers = [int(num) for num in integers]

    return integers


with open("input.txt","r") as f:
    inp = [line.strip() for line in f.readlines()]
s=0
cardNum =0
record = defaultdict(lambda: 1)
for line in inp:

    game = line.split(": ")[1].split(" | ")
    a = extract_integers(game[0])
    b = extract_integers(game[1])

    p = len(set(a) & set(b))
    s+=floor(2**(p-1))

    for i in range(cardNum+1,cardNum+p+1):
        record[i] = record[i] + record[cardNum]

    cardNum+=1

print(s)
print(sum(record.values())+1)



