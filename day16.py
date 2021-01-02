from day16input import *

typestrings = typesstring.split('\n')
data = {}
for s in typestrings:
    splitted = s.split(':')
    type = splitted[0]
    ranges = splitted[1].split(' or ')
    range1 = ranges[0][1:]
    range2 = ranges[1]
    values1 = range1.split('-')
    values2 = range2.split('-')
    value = [range( int(values1[0]), int(values1[1])+1 ),range( int(values2[0]), int(values2[1])+1 )]
    data[type] = value

myticket = [int(x) for x in ticketstring.split(',')]

nearbyticketslines = nearbyticketstring.split('\n')
nearbytickets = []

ticketgroups = [myticket]

for l in nearbyticketslines:
    nrs = l.split(',')
    nextticket = []
    for nr in nrs:
        nearbytickets.append(int(nr))
        nextticket.append(int(nr))

    ticketgroups.append(nextticket)

alltickets = (myticket + nearbytickets).copy()
for nr in alltickets.copy():
    for rangepairs in data.values():
        if nr in rangepairs[0] or nr in rangepairs[1]:
            alltickets.remove(nr)
            break

#Answer 1
print(sum(alltickets))

#Part2
#Removeall bad tickets
for ticket in ticketgroups.copy():
    for nr in ticket:
        if nr in alltickets:
            ticketgroups.remove(ticket)

#Create columns of valid values
columnValues = {}
for column in range(0,len(ticketgroups[0])):
    columnValues[column]=[]
    for row in range(0,len(ticketgroups)):
        columnValues[column].append(ticketgroups[row][column])

#Return correct types for column
def validTypes(column):
    answer = []
    for type, rangepairs in data.items():
        valid = True
        for row in column:
            if row not in rangepairs[0] and row not in rangepairs[1]:
                valid = False
                break
        if valid:
            answer.append(type)
    return answer

#Pairs of columns and all its valid types
columnTypes = [ (column, validTypes(value)) for column, value in columnValues.items() ]

def setLength(tuple):
    return len(tuple[1])
columnTypes.sort(key=setLength)

def eliminator(tupleList, answer):
    if len(tupleList) == 0:
        return answer

    type = tupleList[0][1][0]
    answer[tupleList[0][0]] = type
    tupleList.remove(tupleList[0])

    for tuple in tupleList:
        if type in tuple[1]:
            tuple[1].remove(type)

    tupleList.sort(key=setLength)
    return eliminator(tupleList, answer)

finalMap = eliminator(columnTypes,{})
#print(finalMap)

answer = 1
for column in range(0,len(myticket)):
    if "departure" in finalMap[column]:
        answer *= myticket[column]

print(answer) #answer 2