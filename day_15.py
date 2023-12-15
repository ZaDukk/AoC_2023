with open("input.txt","r") as f:
    inp = f.read().strip("\n")

operations = inp.split(",")

def hash(operations):
    ct=0
    for char in operations:
        ct += ord(char)
        ct = (ct * 17) % 256
    return ct


p1=0
p2=0


boxes = [[] for i in range(256)]
labelToLens = {}

for operation in operations:
    p1+=hash(operation)
    if "=" in operation:
        label,num =operation.split("=")[0],int(operation.split("=")[1])
        labelToLens[label]=num
        index = hash(label)
        if label in boxes[index]:
            continue
        boxes[index].append(label)

    else:
        label = operation[:-1]
        index =hash(label)
        if label not in boxes[index]:
            continue
        boxes[index].remove(label)

for b,box in enumerate(boxes):
    for s,slot in enumerate(box):
        p2+= (b+1)*(s+1)*labelToLens[slot]


print(p1)
print(p2)