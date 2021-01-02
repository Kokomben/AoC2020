from day18input import *

#https://www.geeksforgeeks.org/operator-overloading-in-python/
#https://www.programiz.com/python-programming/precedence-associativity
#__sub__ (-) has same precedense as __add__ (+)
#__pow__ (**) has the second highest precedence after ()
class Customnr(int):
    def __add__(self, nr):
        return Customnr(int(self) + nr ) #+ adds them together
    def __sub__(self, nr):
        return Customnr(int(self) * nr ) #- multiplies them (same precedence as "+")
    def __mul__(self, nr):
        return Customnr(int(self) * nr ) # multiplies them (before + or -)
    def __pow__(self, nr):
        return Customnr(int(self) + nr ) # add them together (before anything else)

#Swap all numbers to "Customnr"
def convertNrsToCustom(line):
    newlineList = []
    for item in line:
        if item.isnumeric():
            newlineList.append("Customnr("+item+")")
        else:
            newlineList.append(item)
    return "".join(newlineList)

#change * to -, convertNrs and eval
def part1eval(line):
    line = line.replace("*","-")
    line = convertNrsToCustom(line)
    return eval(line)

#change + to **, convertNrs and eval
def part2eval(line):
    line = line.replace("+","**")
    line = convertNrsToCustom(line)
    return eval(line)

#part1
lines = inputString.split("\n")
sum1 = 0
sum2 = 0
for line in lines:
    sum1 += part1eval(line)
    sum2 += part2eval(line)

print(sum1)
print(sum2)
