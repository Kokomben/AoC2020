from day20input import *

#None -> {int:[[char]]}
def buildTiles():
    tilesString = inputString.split("\n\n")
    tiles = {}
    for t in tilesString:
        id = int(t[5:9]) #int
        tiles[id] = [ list(row) for row in t[11:].split("\n") ] #list of lists(rows) of strings (chars)
    return tiles

#[[char]] len = 10 -> [[char]] len = 4
def getAllBorders(tile): #Top bottom left right
    return [ tile[0], tile[-1], [row[0] for row in tile], [row[-1] for row in tile] ] #list of lists (borders) of strings (chars)

#[[char]] -> [[[char]]] len = 4
def getAllFlips(tile): #itself, upside down, mirrored, mirrored and upside down
    return [ tile, tile[::-1], [ row[::-1] for row in tile ], [ row[::-1] for row in tile[::-1] ] ] #list of lists(tilevalues) of lists (rows) of strings (char)

#Rotate a tile 90 degrees
#[[char]] -> [[char]]
def rotate(tile):
    newtile = [row.copy() for row in tile]
    for x in range(0,len(tile)):
        for y in range(0,len(tile[x])):
            newtile[x][y] = tile[ len(tile[x]) - (y+1) ][x]
    return newtile

#Get all rotations
#[[char]] -> [[[char]]] len = 4
def getAllRotations(tile):
    rotations = [tile]
    current = tile
    for _ in range(0,3):
        newtile = rotate(current)
        rotations.append(newtile)
        current = newtile
    return rotations

#Get all possible transformations of a tile
#[[char]] -> [[[char]]] len = 8
def getAllTransformations(tile):
    transformations = [] #len = 16
    result = [] #len = 8

    for flip in getAllFlips(tile): #All rotations for every flip
        transformations.extend(getAllRotations(flip))

    for tile in transformations:
        if tile not in result: #Exclude all duplicates
            result.append(tile)

    return result

#Decent Representation of each possible tile (transformation). Stored in dictionary (just incase) Key = tileId + transformID, value = Tiledata
class Tiledata:
    def __init__(self, tileId, transformID, tile, topborder, bottomborder, leftborder, rightborder):
        self.tileId = tileId #Given id
        self.transformID = transformID #0-7
        self.tile = tile #Data #[[char]]
        self.leftborder = leftborder #str
        self.topborder = topborder
        self.bottomborder = bottomborder
        self.rightborder = rightborder

#Builder. Runs once
def getData(tiles):
    result = {}
    for id, tile in tiles.items():
        transformId = 0
        for transformation in getAllTransformations(tile):
            currentTile = transformation
            bordersList = getAllBorders(currentTile) #Borders become strings for comparision purposes
            result[ str(id) + "_" + str(transformId) ] = Tiledata(id, transformId, currentTile, "".join(bordersList[0]), "".join(bordersList[1]), "".join(bordersList[2]), "".join(bordersList[3]))
            transformId += 1
    return result

#initialize the square board
def initBoard(length):
    board = {}
    for x in range(0,length):
        for y in range(0, length):
            board[(x,y)] = None
    return board

#Builds the board by trying to start with every tile and finding one that fits and so on. Returns the correct board if it is successful
#Params All tiles dict, current board, position on the board, maximum index (square x==y), set of tileIds on board, nr of total tiles.
def recBuilder(tileData, board, postuple, maxIndex, onBoard, nrOfTiles):
    x = postuple[0]
    y = postuple[1]

    #FinalCase
    if len(onBoard) == nrOfTiles - 1 and x == maxIndex and y == maxIndex:
        prevBottom = board[(x-1, y)].bottomborder
        prevRight = board[(x, y-1)].rightborder
        for tile in tileData.values():
            if tile.tileId not in onBoard and tile.leftborder == prevRight and tile.topborder == prevBottom:
                board[(x,y)] = tile
                return [True, board] #Success
        return [False, board]

    nextX = x + 1 if y == maxIndex else x
    nextY = 0 if y == maxIndex else y+1
    results = []

    if x == 0:

        if y == 0: #First case
            #Try all
            for tile in tileData.values():
                nextBoard = board.copy()
                nextBoard[(x,y)] = tile
                nextOnBoard = onBoard.copy()
                nextOnBoard.add(tile.tileId)
                result = recBuilder(tileData, nextBoard, (nextX, nextY), maxIndex, nextOnBoard, nrOfTiles)
                if result[0] == True:
                    return result #Returns first sucessfull result (should only be one)

            return [False, board] #Should never happen
        
        else:
            #Try those that fit previous right border
            prevRight = board[(x, y-1)].rightborder
            for tile in tileData.values():
                if tile.tileId not in onBoard and tile.leftborder == prevRight:
                    nextBoard = board.copy()
                    nextBoard[(x,y)] = tile
                    nextOnBoard = onBoard.copy()
                    nextOnBoard.add(tile.tileId)
                    result = recBuilder(tileData, nextBoard, (nextX, nextY), maxIndex, nextOnBoard, nrOfTiles)
                    results.append(result)
            
            for r in results:
                if r[0] == True:
                    return r

            return [False, board]

    else:

        if y == 0:
            #Try those that fit previous bottom
            prevBottom = board[(x-1, y)].bottomborder
            for tile in tileData.values():
                if tile.tileId not in onBoard and tile.topborder == prevBottom:
                    nextBoard = board.copy()
                    nextBoard[(x,y)] = tile
                    nextOnBoard = onBoard.copy()
                    nextOnBoard.add(tile.tileId)
                    result = recBuilder(tileData, nextBoard, (nextX, nextY), maxIndex, nextOnBoard, nrOfTiles)
                    results.append(result)

            for r in results:
                if r[0] == True:
                    return r

            return [False, board]

        else:
            #Try those that fit previous right and previous bottom border
            prevBottom = board[(x-1, y)].bottomborder
            prevRight = board[(x, y-1)].rightborder
            for tile in tileData.values():
                if tile.tileId not in onBoard and tile.topborder == prevBottom and tile.leftborder == prevRight:
                    nextBoard = board.copy()
                    nextBoard[(x,y)] = tile
                    nextOnBoard = onBoard.copy()
                    nextOnBoard.add(tile.tileId)
                    result = recBuilder(tileData, nextBoard, (nextX, nextY), maxIndex, nextOnBoard, nrOfTiles)
                    results.append(result)

            for r in results:
                if r[0] == True:
                    return r

            return [False, board]        
                

tiles = buildTiles() #All given tiles
data = getData(tiles) #All possible tiles
length = int( len(tiles) ** 0.5 ) #Length of the board sqrt of nr of tiles
board = initBoard(length) #Square board maxX = length-1, maxY = length-1, topleft = (0,0)

result = recBuilder(data, board, (0,0), length-1, set(), len(tiles))
finalBoard = result[1] if result[0] else None #The actual correct board of tiles

#Part1 answer (multiply the tile ids of all corners together)
if result[0]:
    print( finalBoard[(0,0)].tileId * finalBoard[(0, length-1)].tileId * finalBoard[(length-1, 0)].tileId * finalBoard[(length-1, length-1)].tileId )

####################################################################

#Part 2
def removeBorders(tile):
    newtile = []
    #Append all rows apart from the first and last
    for i, row in enumerate(tile):
        if i > 0 and i < len(tile) -1:
            newtile.append(row.copy())
    
    #Remove the first and last column of all rows
    for row in newtile:
        del row[0]
        del row[len(row)-1]
    return newtile


#Build the actual image [[char]]
def buildImage(board, length):
    picture = [[]]
    rowcount = 0
    for y in range(0,length):
        for i in range(0,8):
            for x in range(0,length):
                picture[rowcount].extend( board[(x,y)].tile[i] )
                picture.append([])
            rowcount += 1

    for i in range(0, len(picture)):
        if len(picture[i]) == 0:
            picture = picture[:i] #Remove all empty rows at the end
            break

    return picture

#Defitnition of each "#" in the monster (min offset for X, min offset for Y) as well as maximum required offsets for monster to exist
def mosterCondition(monster):
    result = []
    monsterRows = monster.split("\n")
    for y, row in enumerate(monsterRows):
        for x, char in enumerate(row):
            if char == "#":
                result.append((y,x))
    return result

#Check the rules one by one given an initial offset in both directions
def checkIfMonster(intitalX, initialY, picture, rules, maxIndex):
    rule = rules[0]
    if initialY + rule[0] > maxIndex or intitalX + rule[1] > maxIndex: #Monster does not fit
        return False

    if len(rules) == 1:
        rule = rules[0]
        if picture[ initialY + rule[0] ][ intitalX + rule[1] ] == "#":
            return True #Final part of Monster found
        return False

    rule = rules[0]
    if picture[ initialY + rule[0] ][ intitalX + rule[1] ] == "#":
        return checkIfMonster(intitalX, initialY, picture, rules[1:] , maxIndex) #Check next part
    return False

#Finds ammount of monster symbols in picture
def findMonsters(picture, rules):
    monsterSymbols = 0
    firstXOffset = rules[0][1] #Required offset of Y is 0 so it does not matter (monster can have its head at the top)
    maxIndex = len(picture) -1 

    for y in range(0, len(picture)):
        for x in range(0, len(picture[0])):
            if x >= firstXOffset and picture[y][x] == "#": #Could be a monster (first rule check)
                result = checkIfMonster(x - firstXOffset, y, picture, rules[1:], maxIndex) #Check other rules based on cordinates of this check
                if result:
                    monsterSymbols += len(rules) #MonsterSymbols = (nr of "#" in one monster) * monsters

    return monsterSymbols

def part2():

    #Prepare the tiles so that they are in the correct orientation (rotared 90 degrees and mirrored) and without borders
    for tile in finalBoard.values():
        tile.tile = removeBorders( getAllFlips( rotate( tile.tile.copy() ) )[2] )

    picture = buildImage(finalBoard, length) #Assemble the picture [[char]] p[column][row]
    monsterRule = mosterCondition(monster) #Ordered list of (y,x) cordinates to be "#"
    allPictures = getAllTransformations(picture) #All possible "correct pictures"

    #Check all pictures for monsters (only the correct one has monsters)
    correctPicture = None
    for p in allPictures:
        answer = findMonsters(p, monsterRule)
        if answer > 0:
            correctPicture = p
            break
    
    if correctPicture == None:
        return None

    count = 0
    for row in correctPicture: #All pictures have the same ammount of "#" but this feels nicer
        for char in row:
            if char == "#":
                count += 1

    return count - answer #Monster "density"

print(part2())