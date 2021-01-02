from day12input import *

input = input.split("\n")

def getInstructions():
    instructions = []
    for inst in input:
        instructions.append([inst[0],int(inst[1:])])
    return instructions

def part1():

    instructions = getInstructions()
    currentAngle = 0 #East L = +, R = -
    units = {
        "N":0, "S":0, "E":0, "W":0
    }
    correctUnit = {
        0:"E", 90:"N", 180:"W", 270:"S"
    }

    for inst in instructions:
        direction = inst[0]
        value = inst[1]

        if direction in units.keys():
            units[direction] += value
        elif direction == "L" or direction == "R":
            currentAngle = currentAngle + value if direction == "L" else currentAngle - value
            if currentAngle < 0:
                currentAngle = 360 + currentAngle
            if currentAngle >= 360:
                currentAngle = currentAngle - 360
        elif direction == "F":
            units[correctUnit[currentAngle]] += value

    return abs(units["N"] - units["S"]) + abs(units["W"] - units["E"])

def part2():

    instructions = getInstructions()
    waypointUnits = {
        "N":1, "S":0, "E":10, "W":0
    }
    shipUnits = {
        "N":0, "S":0, "E":0, "W":0
    }

    for inst in instructions:
        direction = inst[0]
        value = inst[1]

        if direction in waypointUnits.keys():
            waypointUnits[direction] += value

        elif direction == "L":
            loops = int(value / 90)
            for _ in range(0,loops):
                tempN = waypointUnits["N"]
                waypointUnits["N"] = waypointUnits["E"] 
                waypointUnits["E"] = waypointUnits["S"]
                waypointUnits["S"] = waypointUnits["W"]
                waypointUnits["W"] = tempN

        elif direction == "R":
            loops = int(value / 90)
            for _ in range(0,loops):
                tempN = waypointUnits["N"]
                waypointUnits["N"] = waypointUnits["W"]
                waypointUnits["W"] = waypointUnits["S"]
                waypointUnits["S"] = waypointUnits["E"]
                waypointUnits["E"] = tempN

        elif direction == "F":
            shipUnits["N"] = shipUnits["N"] + value * waypointUnits["N"]
            shipUnits["S"] = shipUnits["S"] + value * waypointUnits["S"]
            shipUnits["W"] = shipUnits["W"] + value * waypointUnits["W"]
            shipUnits["E"] = shipUnits["E"] + value * waypointUnits["E"]


    return abs(shipUnits["N"] - shipUnits["S"]) + abs(shipUnits["W"] - shipUnits["E"])

print(part1())
print(part2())