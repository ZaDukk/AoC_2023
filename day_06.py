import re
def extract_integers(input_string, allow_negative=False):
    pattern = r'-?\d+' if allow_negative else r'\d+'
    integers = re.findall(pattern, input_string)
    integers = [int(num) for num in integers]

    return integers


#part 1 and part 2 use the same code, just edit the text file to get rid of the spaces!
def part1(time, distance):
    s = 0
    for i in range(time):
        a = i * (time - i)
        if a > distance:
            s += 1
    return s

res=1
with open("input.txt","r") as f:
    inp = [line.strip() for line in f.readlines()]

for i, j in zip(extract_integers(inp[0]), extract_integers(inp[0])):
    res*=part1(i,j)

print(res)

