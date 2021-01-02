from day11input import *

input = input.split('\n')
inputrows = input[1:-1]

lastRow = len(inputrows) -  1
lastcolumn = len(inputrows[0]) - 1

#ListofList State[Row[Column]]
def getStartState():
    state = []
    for inputrow in inputrows:
        row = []
        for column in inputrow:
            row.append(column)
        state.append(row)
    return state

####Part 1 Logic
def CheckOccupied(row, column, state):
    nrOfOccupied = 0
    rowsToCheck = [row]
    if row > 0:
        rowsToCheck.append(row-1)
    if row < lastRow:
        rowsToCheck.append(row+1)
    columnsToCheck = [column]
    if column > 0:
        columnsToCheck.append(column - 1)
    if column < lastcolumn:
        columnsToCheck.append(column + 1)
    for r in rowsToCheck:
        for c in columnsToCheck:
            if state[r][c] == '#' and not (r == row and c == column):
                nrOfOccupied += 1
    return nrOfOccupied

def ShouldBeOccupied(row, column, state):
    return state[row][column] == 'L' and CheckOccupied(row, column, state) == 0

def ShouldBeEmpty(row, column, state):
    return state[row][column] == '#' and CheckOccupied(row, column, state) >= 4


####Part 2 Logic

#1 2 3
#4 L 5
#6 7 8

def checkD1(row, column, state):
    if row < 0 or column < 0:
        return False        
    return state[row][column] == '#' if state[row][column] != '.' else checkD1(row-1, column-1, state)

def checkD2(row, column, state):
    if row < 0:
        return False        
    return state[row][column] == '#' if state[row][column] != '.' else checkD2(row-1, column, state)

def checkD3(row, column, state):
    if row < 0 or column > lastcolumn:
        return False        
    return state[row][column] == '#' if state[row][column] != '.' else checkD3(row-1, column+1, state)

def checkD4(row, column, state):
    if column < 0:
        return False        
    return state[row][column] == '#' if state[row][column] != '.' else checkD4(row, column-1, state)

def checkD5(row, column, state):
    if column > lastcolumn:
        return False        
    return state[row][column] == '#' if state[row][column] != '.' else checkD5(row, column+1, state)

def checkD6(row, column, state):
    if row > lastRow or column < 0:
        return False        
    return state[row][column] == '#' if state[row][column] != '.' else checkD6(row+1, column-1, state)

def checkD7(row, column, state):
    if row > lastRow:
        return False        
    return state[row][column] == '#' if state[row][column] != '.' else checkD7(row+1, column, state)

def checkD8(row, column, state):
    if row > lastRow or column > lastcolumn:
        return False        
    return state[row][column] == '#' if state[row][column] != '.' else checkD8(row+1, column+1, state)

def CheckOccupied2(row, column, state):
    matrix = [checkD1(row-1, column-1, state), checkD2(row-1, column, state), checkD3(row-1, column+1, state), checkD4(row, column-1, state),
                checkD5(row, column+1, state), checkD6(row+1, column-1, state), checkD7(row+1, column, state), checkD8(row+1, column+1, state)]
    return matrix.count(True)

def ShouldBeOccupied2(row, column, state):
    return state[row][column] == 'L' and CheckOccupied2(row, column, state) == 0

def ShouldBeEmpty2(row, column, state):
    return state[row][column] == '#' and CheckOccupied2(row, column, state) >= 5


#Change State
def ChangeState(state, part):
    seatsToOccupy = []
    seatsToEmpty = []
    for row in range(0,lastRow+1):
        for column in range(0,lastcolumn+1):
            if part == 2:
                if ShouldBeOccupied2(row, column, state):
                    seatsToOccupy.append({"Row":row,"Column":column})
                if ShouldBeEmpty2(row, column, state):
                    seatsToEmpty.append({"Row":row,"Column":column})
            else:
                if ShouldBeOccupied(row, column, state):
                    seatsToOccupy.append({"Row":row,"Column":column})
                if ShouldBeEmpty(row, column, state):
                    seatsToEmpty.append({"Row":row,"Column":column})

    newState = state.copy()
    for seat in seatsToOccupy:
        newState[seat["Row"]][seat["Column"]] = '#'
    for seat in seatsToEmpty:
        newState[seat["Row"]][seat["Column"]] = 'L'

    return [newState, len(seatsToOccupy) == 0 and len(seatsToEmpty) == 0] #New state and Changed (bool)

##Execution
def Run(part, state):
    while True:
        newState = ChangeState(state, part)[0]
        notChanged = ChangeState(state, part)[1]
        if notChanged:
            break
        else:
            state = newState

    count = 0
    for r in range(0,lastRow+1):
        for c in range(0,lastcolumn+1):
            if state[r][c] == '#':
                count += 1

    return count

print( Run(1, getStartState()) )
print( Run(2, getStartState()) )
