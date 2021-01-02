input = "1,20,8,12,0,14"
inputnrs = input.split(',')

def findprevious(spoken, nr):
    for turn in reversed(spoken):
        if turn[1] == nr:
            return turn[2]
    return -1

def findpreviousdiff(spoken, nr):
    result = []
    for turn in reversed(spoken):
        if turn[1] == nr:
            result.append(turn[0])
        if len(result) == 2:
            return result[0] - result[1]

def part1():
    spoken = [] #[count, nr, lastcount]
    count = 1
    while len(spoken) < 2020:
        if count < len(inputnrs)+1:
            spoken.append( [count, int(inputnrs[count-1]), 0] )
            count += 1
            continue

        if spoken[count-2][2] == 0:
            spoken.append( [count, 0, findprevious(spoken, 0)+1] )
            count +=1
        else:
            next = findpreviousdiff(spoken, spoken[count-2][1])
            spoken.append([ count, next, findprevious(spoken, next)+1 ])
            count +=1

    return spoken[-1][1]

#dictionarys should be faster than list check loops since they are basically hashed per default
def part2(finalturn):
    spoken=inputnrs.copy()
    history = {}
    for i, nr in enumerate(spoken):
        history[int(nr)] = i + 1

    turn = len(spoken) + 1
    previous = spoken[-1]

    while turn <= finalturn:

        if previous in history.keys(): #Check history first
            nr = (turn - 1) - history[previous]
        else:
            nr = 0

        history[previous] = turn - 1 #Update history

        previous = nr
        turn += 1

    return previous

print(part1())
#print(part2(2020))
print(part2(30000000)) #about 10 sec



