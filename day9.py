from day9input import *

inputstring = input.split('\n')
input = []
for x in inputstring:
    input.append(int(x))
inputToCheck = input[25:]

def checkValidity(nr, place):
    nrSet = input[place-25:place]
    for i in nrSet:
        secondSet = nrSet.copy()
        secondSet.remove(i)
        for j in secondSet:
            if nr == i + j:
                return True
    return False

firstAnswer = 0

for i, nr in enumerate(inputToCheck):
    if not checkValidity(nr,i+25):
        firstAnswer = nr
        break

print(firstAnswer)

def sum(start, end):
    r = input[start:end+1]
    sum = 0
    for i in r:
        sum = sum + i
    return sum

start = 0
end = 1
for i, x in enumerate(input):
    if firstAnswer == sum(start,end):
        break
    elif sum(start,end) < firstAnswer:
        end = end + 1
    else:
        start = start + 1

range = input[start:end+1]
answer2 = min(range) + max(range)
print(answer2)        