initialStateString = """.###..#.
##.##...
....#.#.
#..#.###
...#...#
##.#...#
#..##.##
#......."""

initialRows = initialStateString.split('\n')
initialRows = [list(row) for row in initialRows]

def getNeighbors(x, y, z):
    result = []
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            for k in range(z-1,z+2):
                if i == x and j == y and k == z:
                    continue
                result.append((i,j,k))
    return result

def getNeighbors2(x, y, z, w):
    result = []
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            for k in range(z-1,z+2):
                for v in range(w-1, w+2):
                    if i == x and j == y and k == z and v == w :
                        continue
                    result.append((i,j,k,v))
    return result

def extendState(state):
    x, y, z = zip(*state.keys())
    xMin, xMax = min(x), max(x)
    yMin, yMax = min(y), max(y)
    zMin, zMax = min(z), max(z)
    for i in range(xMin-1,xMax+2):
        for j in range(yMin-1,yMax+2):
            for k in range(zMin-1,zMax+2):
                if (i,j,k) not in state:
                    state[(i,j,k)] = '.'
    return state

def extendState2(state):
    x, y, z, w = zip(*state.keys())
    xMin, xMax = min(x), max(x)
    yMin, yMax = min(y), max(y)
    zMin, zMax = min(z), max(z)
    wMin, wMax = min(w), max(w)
    for i in range(xMin-1,xMax+2):
        for j in range(yMin-1,yMax+2):
            for k in range(zMin-1,zMax+2):
                for v in range(wMin-1,wMax+2):
                    if (i,j,k,v) not in state:
                        state[(i,j,k,v)] = '.'
    return state

def printState(state):
    x, y, z = zip(*state.keys())
    for k in sorted(set(z)):
        print("z=" + str(k))
        for i in sorted(set(x)):
            for j in sorted(set(y)):
                print(state[(i,j,k)], end="")
            print("")
        print("")

def printState2(state):
    x, y, z, w = zip(*state.keys())
    for v in sorted(set(w)):
        for k in sorted(set(z)):
            print("z=" + str(k) + " w=" + str(v))
            for i in sorted(set(x)):
                for j in sorted(set(y)):
                    print(state[(i,j,k,v)], end="")
                print("")
            print("")
        print("")


def getInitState():
    xlen = len(initialRows)
    ylen = len(initialRows[0])
    xshift = 0 - int ( ( xlen - 1 ) / 2 )
    yshift = 0 - int ( ( ylen -1 ) / 2 )

    initialState = { #Using dictionary to avoid suffering (x,y,z):#/.
        (x + xshift, y + yshift, 0) : initialRows[x][y]
        for x in range(0, xlen)
        for y in range(0, ylen)
    }

    return initialState

def getInitState2():
    xlen = len(initialRows)
    ylen = len(initialRows[0])
    xshift = 0 - int ( ( xlen - 1 ) / 2 )
    yshift = 0 - int ( ( ylen -1 ) / 2 )

    initialState = { #Using dictionary to avoid suffering (x,y,z):#/.
        (x + xshift, y + yshift, 0, 0) : initialRows[x][y]
        for x in range(0, xlen)
        for y in range(0, ylen)
    }

    return initialState

def shouldBeActive(status, activeNeighbors):
    return (status == "." and activeNeighbors == 3) or ( status == "#" and 2 <= activeNeighbors <= 3 )

def cycleState(state, iterations):
    #printState(state)
    if iterations < 1:
        return state

    state = extendState(state)
    newState = {}

    for cordinate, status in state.items():
        active = 0
        neighbors = getNeighbors(*cordinate)

        for neighbor in neighbors:
            if neighbor in state.keys() and state[neighbor] == "#":
                active = active + 1

        if shouldBeActive(status, active):
            newState[cordinate] = "#"
        else:
            newState[cordinate] = "."
        
    return cycleState(newState, iterations-1)

def cycleState2(state, iterations):
    #printState2(state)
    if iterations < 1:
        return state

    state = extendState2(state)
    newState = {}

    for cordinate, status in state.items():
        active = 0
        neighbors = getNeighbors2(*cordinate)

        for neighbor in neighbors:
            if neighbor in state.keys() and state[neighbor] == "#":
                active = active + 1

        if shouldBeActive(status, active):
            newState[cordinate] = "#"
        else:
            newState[cordinate] = "."
        
    return cycleState2(newState, iterations-1)

def countActive(state):
    return list(state.values()).count("#")
        

print(countActive(cycleState(getInitState(),6)))
print(countActive(cycleState2(getInitState2(),6)))