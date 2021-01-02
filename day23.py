inputString = "389547612"

input = [int(x) for x in inputString] #cup values

def buildState(input):
    state = {} #key = cup, value = index in input of next cup
    last = input[-1]
    for i, v in enumerate(input):
        state[v] = i+1 if v != last else 0
    return state

def doMove(input, state, currentCup, minValue, maxValue):
    #Pick up all cups based on current cup
    pickupIndex1 = state[currentCup]
    pickupCup1 = input[pickupIndex1]
    pickupIndex2 = state[pickupCup1]
    pickupCup2 = input[pickupIndex2]
    pickupIndex3 = state[pickupCup2]
    pickupCup3 = input[pickupIndex3]

    #Select distination cup
    destinationCup = currentCup - 1 if currentcup != minValue else maxValue
    while destinationCup in [pickupCup1, pickupCup2, pickupCup3]:
        destinationCup = destinationCup - 1 if destinationCup > minValue else maxValue         
    
    #Repoint state
    state[currentCup] = state[pickupCup3] #After currentcup comes the cup after the last picked up cup
    state[pickupCup3] = state[destinationCup] #After the last picked up cup comes the distinationCup
    state[destinationCup] = pickupIndex1 #After the distinationcup comes the first picked up cup
    #The rest stay the same.

    currentCup = input[state[currentCup]] #New currentcup (cup after the last picked up cup)
    return [state, currentCup]


state = buildState(input)
currentcup = input[0]
for i in range(0,100):
    result = doMove(input, state, currentcup, 1, 9)
    state = result[0]
    currentcup = result[1]

cup = 1
cupstr = ""
for i in range(0,len(input)):
    cup = input[state[cup]]
    cupstr += str(cup)
print(cupstr[:-1])

#Part 2
for i in range( max(input) + 1, 1000001 ):
    input.append(i)

state = buildState(input)

currentcup = input[0]
for i in range(0,10000000): #Takes 13 seconds
    result = doMove(input, state, currentcup, 1, 1000000)
    state = result[0]
    currentcup = result[1]

cup1 = input[state[1]]
cup2 = input[state[cup1]]
print(cup1*cup2)