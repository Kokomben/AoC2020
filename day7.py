from day7input import *

input = input.split('\n')
colors = {} #color, nr, color

def getcolors():
    for rule in input:
        contains = rule.index("contain")
        maincolor = rule[:contains-6]
        colors[maincolor] = {}
        getcontent(maincolor, rule[contains+7:])

def getcontent(maincolor, content):
    splitted = content.split(',')
    colors[maincolor]["content"] = {}
    for rule in splitted:
        rule = rule.replace(' bags','').replace(' bag', '').replace('.','')
        nr = rule[1]
        try:
            colors[maincolor]["content"][rule[3:]] = int(nr)
        except:
            colors[maincolor]["content"]["None"] = True


getcolors() #Build Data

def findammount(color, searchedcolor):
    content = colors[color]["content"]

    if "None" in content: #No colors count ends
        return 0

    if searchedcolor in list(content.keys()): #Found color add value
        return content[searchedcolor]

    result = 0
    for key in list(content.keys()): #Does not have color checking each color it has
        result = result + findammount(key, searchedcolor)
    return result

def findammountOfBags(color):
    content = colors[color]["content"]

    if "None" in content: #No colors count ends
        return 0

    result = 0
    for key, value in list(content.items()):
        result = result + value + (value * findammountOfBags(key))

    return result

#test = findammount(0, "wavy yellow","shiny gold")
#print(test)

answer1 = 0
for color in list(colors.keys()):
    ammount = findammount(color,"shiny gold")
    if ammount > 0:
        answer1 = answer1 + 1

print(answer1)

answer2 = findammountOfBags("shiny gold")
print(answer2)
