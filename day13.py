input1 = "1000067"
input2= "17,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,439,x,29,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,787,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,19"

def part1():
    minTime = int(input1)
    intervalls = list(filter( ("x").__ne__, input2.split(',') ) )
    for i in range(0, len(intervalls )):
        intervalls[i] = int (intervalls[i])

    busses = intervalls.copy()

    answer1 = 0
    loop = True
    while loop:
        validNumbers = []
        for i in range(0,len(busses)):
            if intervalls[i] < minTime:
                intervalls[i] += busses[i]
            else:
                validNumbers.append(intervalls[i])

        if len(validNumbers) == len(intervalls):
            best = min(validNumbers)
            i = intervalls.index(best)
            answer1 = ( best - minTime ) * busses[i]
            #print([best, minTime, i, busses[i]])
            loop = False 

    return answer1

print(part1())

#Part 2
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

input = input2.split(',')
busses = []
for i, buss in enumerate(input): #Remove all "x" and keep original index
    if buss != 'x':
        busses.append((i,int(buss)))

def isDeparting(time, buss):
    return time % buss == 0 #If bus departs at a time the time is evenly devisible by the bus nr

time = 0
increment = busses[0][1] #Increment time by a valid number that is evenly devisible for all busses so far, starts with intervall of first buss

for i, buss in busses[1:]:
    while not isDeparting(time + i, buss):
        time = time + increment #Increase the time by increment for next check so it does not brake the previous busses
    increment = abs(increment*buss) // gcd(increment, buss) #Make increment evenly devisible for this buss too (LCD)

print(time)
