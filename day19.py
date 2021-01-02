from day19input import *
rulesList = rulesString.split("\n")
messageList = messageString.split("\n")

class Rule:
    def __init__(self, char, rulesets):
        self.char = char
        self.rulesets = rulesets

rulesDict = {} #The rules
def printRules():
    for key, value in rulesDict.items():
        print(str(key) + " " + str(value.char) + " " + str(value.rulesets))


def match(message, rulenrs):
    if len(message) == 0 and len(rulenrs) == 0: #If both finished at same time ok
        return True
    elif len(message) == 0 or len(rulenrs) == 0: #If not fail
        return False
    
    rule = rulesDict[rulenrs[0]] #First rule of list

    if rule.char: #If it is a char rule
        if message[0] == rule.char: #match
            return match(message[1:], rulenrs[1:]) # Move on (if nothing left in both ok)
        else:
            return False # wrong char

    result = False
    for set in rule.rulesets: #For each set where (set|set) add on the other rules if any and "or" it (|)
        result = result or match(message, set + rulenrs[1:])
    return result

for rule in rulesList:
    splitted = rule.split(":")
    nr = int(splitted[0])
    if "\"" in splitted[1]:
        rulesDict[nr] = Rule( splitted[1].replace("\"","").replace(" ",""), None )
    else:
        rulesets = []
        for part in splitted[1].split("|"):
            nrs = []
            for n in part.split():
                nrs.append(int(n))
            rulesets.append(nrs)
        rulesDict[nr] = Rule(None, rulesets)

#printRules()

def printSum(rulelist):
    sum = 0
    for message in messageList:
        if match(message,rulelist):
            sum +=1
    print(sum)

#Part1
printSum([0])

#Part2
rulesDict[8] = Rule(None, [[42],[42,8]])
rulesDict[11] = Rule(None, [[42, 31],[42,11,31]])
printSum([0])
