from day24input import *
inputrows = inputString.split("\n")

def getNextTile(tile, data):
    if data[0] == "e":
        tile = (tile[0]+2, tile[1])
        data = data[1:]
    elif data[0] == "s" and data[1] == "e":
        tile = (tile[0]+1, tile[1]+1)
        data = data[2:]
    elif data[0] == "s" and data[1] == "w":
        tile = (tile[0]-1, tile[1]+1)
        data = data[2:]
    elif data[0] == "w":
        tile = (tile[0]-2, tile[1])
        data = data[1:]
    elif data[0] == "n" and data[1] == "w":
        tile = (tile[0]-1, tile[1]-1)
        data = data[2:]
    elif data[0] == "n" and data[1] == "e":
        tile = (tile[0]+1, tile[1]-1)
        data = data[2:]
    return [tile, data]

def part1():
    state = {}
    for inputrow in inputrows:
        row = list(inputrow)
        tile = (0,0)
        while len(row) != 0:
            result = getNextTile(tile, row)
            tile = result[0]
            row = result[1]
        if tile not in state:
            state[tile] = "Black"
        else:
            state[tile] = "Black" if state[tile] == "White" else "White"

    count = 0
    for color in state.values():
        if color == "Black":
            count += 1
    return [state, count]

result = part1()
count = result[1]
print(count)

#Part2

#Keeping only black tiles to avoid extending state
blackTiles = set()
state = result[0]
for tile, value in state.items():
    if value == "Black":
        blackTiles.add(tile)

def getNeighbours(tile):
    Etile = (tile[0]+2, tile[1])
    SEtile = (tile[0]+1, tile[1]+1)
    SWtile = (tile[0]-1, tile[1]+1)
    Wtile = (tile[0]-2, tile[1])
    NWtile = (tile[0]-1, tile[1]-1)
    NEtile = (tile[0]+1, tile[1]-1)
    return [Etile, SEtile, SWtile, Wtile, NWtile, NEtile]

#One day iteration
def run(blackTiles):
    nrOfNeighbours = {} #key = tile, value = number of current neighboors of the tile

    for tile in blackTiles: #Initiate black tiles
        nrOfNeighbours[tile] = 0

    #The only relevant tiles are the black ones and their neighbours
    for tile in blackTiles:
        neighboors = getNeighbours(tile)
        for neighboor in neighboors:
            if neighboor not in nrOfNeighbours.keys():
                nrOfNeighbours[neighboor] = 1 #(neighbour of current tile)
            else:
                nrOfNeighbours[neighboor] += 1

    newBlackTiles = set()
    for tile, nr in nrOfNeighbours.items():
        if tile in blackTiles and nr == 1 or nr == 2:
            newBlackTiles.add(tile) #Stay Black
        elif tile not in blackTiles and nr== 2: 
            newBlackTiles.add(tile) #Become black

    return newBlackTiles

for _ in range(0,100):
    blackTiles = run(blackTiles)

print(len(blackTiles))
