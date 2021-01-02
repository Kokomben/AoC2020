from day1input import *

input = input.split('\n')
input = input[1:len(input)-1]
for i,x in enumerate(input):
    input[i] = int(x)

answer1 = []
answer2 = []
for x in input:
    tempInput = input.copy()
    tempInput.remove(x)
    for y in tempInput:
        if x + y == 2020:
            answer1.append([x*y,x,y])
        secondtemp = tempInput.copy()
        secondtemp.remove(y)
        for z in secondtemp:
            if x + y + z == 2020:
                answer2.append([x*y*z,x,y,z])

print(answer1[0][0])
print(answer2[0][0])