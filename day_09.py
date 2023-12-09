import re
def extract_integers(input_string, allow_negative=False):
    pattern = r'-?\d+' if allow_negative else r'\d+'
    integers = re.findall(pattern, input_string)
    integers = [int(num) for num in integers]

    return integers

with open("input.txt","r") as f:
    inp = [extract_integers(line,True) for line in f.readlines()]

def getDifferences(sequence):
	if sum(sequence)==0 and [sequence[0]]*len(sequence)==sequence:
		return 0
	newSequence = []
	for i in range (len(sequence)-1):
		newSequence.append(sequence[i+1]-sequence[i])
	#first time using recursion for this year!
	return sequence[-1] + getDifferences(newSequence)


print(f"p1: {sum(getDifferences(line) for line in inp)}")
print(f"p2: {sum(getDifferences(line[::-1]) for line in inp)}")
