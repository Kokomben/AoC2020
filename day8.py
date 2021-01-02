from day8input import *

instructions = input.split("\n")

def runBoot(instructions):
    executedList = []
    acc = 0
    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        command = instruction[:3]
        sign = instruction[4]
        nr = int(instruction[5:])

        if i in executedList:
            return [False, str(acc)]

        if command == "acc":
            if sign == "+":
                acc = acc + nr
            else:
                acc = acc - nr
            executedList.append(i)
            i = i + 1
        elif command == "jmp":
            executedList.append(i)
            if sign == "+":
                i = i + nr
            else:
                i = i - nr
        else:
            executedList.append(i)
            i = i + 1
    return [True, str(acc)]

print("answer1 " + runBoot(instructions)[1])

newInstructions = []
for i, instruction in enumerate(instructions):
    splitted = instruction.split(' ')
    if splitted[0] == "nop":
        newInstruction = " ".join(["jmp",splitted[1]])
    elif splitted[0] == "jmp":
        newInstruction = " ".join(["nop",splitted[1]])
    else:
        continue

    newInstructions = instructions.copy()
    newInstructions[i] = newInstruction

    r = runBoot(newInstructions)
    if r[0]:
        print("answer2 " + str(r[1]) + ". Instruction " + str(i))
        break
