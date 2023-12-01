import re



def extract_integers(input_string):
    nums = []
    for c in input_string:
        if c.isdigit():
            nums.append(int(c))
    return nums

with open("input.txt","r") as f:
    inp = [line.strip() for line in f.readlines()]


#part 1
sum =0
last = []

for x in inp:
    t = extract_integers(x)
    sum+=(int(f"{t[0]}{t[-1]}"))


print(sum)


sum=0

#part2
def returnDigits(s):
    numsAsWords = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    res = []

    for length in range(5, 2, -1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring in numsAsWords:
                res.append((i, numsAsWords[substring]))

    res.sort(key=lambda x: x[0])
    return [digit for _, digit in res]

for line in inp:
    currectString = ""
    nums = []
    for c in line:
        if c.isdigit():
            t = returnDigits(currectString)
            nums.extend(t)
            nums.append(int(c))
            currectString=""
        else:
            currectString+=c
    t = returnDigits(currectString)
    nums.extend(t)

    sum+=int(f"{nums[0]}{nums[-1]}")

print(sum)