from day10input import *

#Init
s = s.split('\n')
input = []
for i in s:
    input.append(int(i))

input.sort()
input.insert(0,0) #start
input.append(max(input)+3) #end

#Part 1
curr = diff1 = diff2 = diff3 = 0
for i in input:
    if i - curr == 1:
        diff1 +=1
    elif i - curr == 2:
        diff2 +=1
    elif i - curr == 3:
        diff3 +=1
    curr = i
print(diff1*diff3)

##Part 2
ways = [1]
for i in range(1,len(input)):
    ways.append(0)

for i in range(1,len(ways)):
    for j in range(i-3 if i>3 else 0,i): 
        if input[i] - input[j] >= 1  and input[i] - input[j] <= 3:
            ways[i] = ways[i] + ways[j]

print(ways[len(ways)-1]) #Final