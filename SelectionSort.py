list = [7,4,2,78,9,4,2,67,8,2]

for i in range(len(list)):
    smallindex = i
    for k in range(i, len(list)):
        if list[smallindex] < list[k]:
            smallindex = k
    
    tempvalue = list[i]
    list[i] = list[smallindex]
    list[smallindex] = tempvalue

print(list) 