from day14input import *

input = inputString.split('\n')

def decToBinList(value):
    stringlist = list(str(bin(value))[2:]) 
    result = []
    for i, x in enumerate(reversed(stringlist)):
        result.append((i, int(x)))
    return result

def maskToList(mask):
    result = []
    for i, x in enumerate(reversed(mask)):
        result.append((i, int(x) if x != 'X' else x))
    return result

def getOperations():
    operations = []
    for line in input:
        if line[1] == 'e':
            type = 'mem'
        else:
            type = 'mask'

        if type == 'mem':
            s = line.index('[')
            e = line.index(']')
            memvalue = int(line[s+1:e])
            value = int(line.split('=')[1][1:])
            binlist = decToBinList(value)
            operations.append({"type":type, "memvalue":memvalue, "value":value, "binlist":binlist })

        else:
            value = line.split('=')[1][1:]
            operations.append({"type":type, "value":maskToList(value) })
    return operations

operations = getOperations()

#Part1
def part1(operations):

    mask = operations[0]["value"]
    mems = {}

    for op in operations[1:]:
        if op["type"] == "mask":
            mask = op["value"]
            continue

        memvalue = op["memvalue"]
        binlist = op["binlist"]
        result = []
        for i, _ in mask:
            if mask[i][1] == 'X':
                if i >= len(binlist):
                    result.append( '0' )
                    continue
                result.append( str( binlist[i][1] ) )
            else:
                result.append( str(mask[i][1]) )
        result.reverse()
        mems[memvalue] = int("".join( result ),2)

    sum = 0
    for x in mems.values():
        sum = sum + x
    return sum

#Part2

def buildmems(mems):
    currentmem = None
    for mem in mems:
        if 'X' in mem:
            currentmem = mem

    if currentmem == None:
        result = []
        for mem in mems:
            result.append(int("".join(mem),2))
        return result
    
    i = currentmem.index('X')
    newmem1 = currentmem.copy()
    newmem2 = currentmem.copy()
    newmem1[i] = '0'
    newmem2[i] = '1'
    mems.remove(currentmem)
    mems.append(newmem1)
    mems.append(newmem2)
    return buildmems(mems)
    

def part2(operations):
    mask = operations[0]["value"]
    mems = {}
    for op in operations[1:]:
        if op["type"] == "mask":
            mask = op["value"]
            continue

        memvalue = op["memvalue"]
        binmem = list( str(bin(memvalue))[2:] )
        binmem.reverse()

        result = []
        for i, b in mask:
            if b == 0:
                if i >= len(binmem):
                    result.append('0')
                else:
                    result.append(binmem[i])
            elif b == 1:
                result.append('1')
            else:
                result.append('X')

        result.reverse()
        allmems = buildmems([result])

        for mem in allmems:
            mems[mem] = op["value"]

        sum = 0
        for value in mems.values():
            sum = sum + value

    return sum

print(part1(operations))
print(part2(operations))