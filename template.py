import re
def extract_integers(input_string, allow_negative=False):
    pattern = r'-?\d+' if allow_negative else r'\d+'
    integers = re.findall(pattern, input_string)
    integers = [int(num) for num in integers]

    return integers


with open("input.txt","r") as f:
    inp = [line.strip() for line in f.readlines()]

