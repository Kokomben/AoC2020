from day3input import *

input = input.replace(' ', '').split('\n')
input = input[1:len(input)-1]

def check(right, down):
    trees = 0
    horizontal = 0
    i = 0
    while i < len(input):
        if i >= len(input) - down:
            break
        nextrow = input[i+down]

        if horizontal + right < len(nextrow):
            horizontal = horizontal + right
        else:
            horizontal = horizontal + right - len(nextrow)
        nextPoint = nextrow[horizontal]

        if nextPoint == '#':
            trees += 1
        i += down
    return trees

answer1 = check(3, 1)
answer2 = check(1, 1) * answer1 * check(5, 1) * check(7, 1) * check(1, 2)

print(answer1)
print(answer2)