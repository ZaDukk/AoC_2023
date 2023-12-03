with open("input.txt","r") as f:
    inp = [line.strip() for line in f.readlines()]

#p1
nums=set()

res=0
vectors = [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(1,1),(1,-1),(-1,1)]

for r in range (len(inp)):
    row = inp[r]
    for c in range (len(row)):
        item = row[c]

        if item.isdigit() or item==".":
            continue
        # item is a symbol
        else:#
            for dr,dc in vectors:
                newRow,newCol = r+dr, c+dc
                #avoid being out of the grid
                if newRow<0 or newRow>=len(inp) or newCol<0 or newCol>=len(row):
                    continue
                #check the bounding box of the symbol for a number
                if inp[newRow][newCol].isdigit():
                    while(True):
                        if (newCol-1)>=0:
                            newCol-=1
                            if not inp[newRow][newCol].isdigit():
                                nums.add((newRow,newCol+1))
                                break
                        else:
                            nums.add((newRow, newCol))
                            break

#print(nums)

for r,c in nums:
    current =""
    current+= inp[r][c]
    while (True):
        if c+1<len(inp):
            c+=1
            if inp[r][c].isdigit():
                current+=inp[r][c]
            else:
                break
        else:
            break
    res+=int(current)



print(res)

print("part 2")
#p2
nums=[]

res=0
vectors = [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(1,1),(1,-1),(-1,1)]

for r in range (len(inp)):
    row = inp[r]
    for c in range (len(row)):
        item = row[c]

        if item!="*":
            continue
        # item is a gear
        else:
            temp = set()
            for dr,dc in vectors:
                newRow,newCol = r+dr, c+dc
                #avoid being out of the grid
                if newRow<0 or newRow>=len(inp) or newCol<0 or newCol>=len(row):
                    continue
                #check the bounding box of the symbol for a number
                if inp[newRow][newCol].isdigit():
                    while(True):
                        if (newCol-1)>=0:
                            newCol-=1
                            if not inp[newRow][newCol].isdigit():
                                temp.add((newRow,newCol+1))
                                break
                        else:
                            temp.add((newRow, newCol))
                            break
            if len(temp)==2:
                nums.append([i for i in temp])

#print(nums)
s =0

for gearPair in nums:
    prod = 1
    for gear in gearPair:
        r, c = gear[0], gear[1]
        current = inp[r][c]
        while (True):
            if c + 1 < len(inp):
                c += 1
                if inp[r][c].isdigit():
                    current += inp[r][c]
                else:
                    break
            else:
                break
        #print(current)
        prod *= int(current)
    s += prod
print(s)