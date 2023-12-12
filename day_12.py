import re
from functools import lru_cache
def extract_integers(input_string, allow_negative=False):
    pattern = r'-?\d+' if allow_negative else r'\d+'
    integers = re.findall(pattern, input_string)
    integers = [int(num) for num in integers]

    return integers
@lru_cache()
def solve(springs, nums):
    # base case
    if len(springs)==0:
        return 1 if len(nums)==0 else 0

    if len (nums)==0:
        return 1 if "#" not in springs else 0


    t = 0

    if springs[0] =="." or springs[0]=="?":
        t += solve(springs[1:], nums)

    if (springs[0] in "#?") and("." not in springs[:nums[0]]) and  (nums[0] <= len(springs))   and ((nums[0] == len(springs) or springs[nums[0]] != "#")):
        t += solve(springs[nums[0] + 1:], nums[1:])

    return t


with open("input.txt","r") as f:
    inp = [line.strip() for line in f.readlines()]

p1=0
p2 =0
for line in inp:
    springs = line.split()[0]
    nums = extract_integers(line)
    p1+=(solve(springs,tuple(nums)))
    p2+=solve("?".join([springs]*5),tuple(nums)*5)

print(f"p1: {p1}\np2: {p2}")

