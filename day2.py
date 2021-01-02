from day2input import *

input = input.replace('\t','').replace(' ', '').split('\n')
input = input[1:len(input)-1]
correctfirst = 0
correctsecond = 0

for item in input:
    splitted = item.split(':')
    password = splitted[1]
    char = splitted[0][len(splitted[0])-1]
    splitted[0] = splitted[0][:len(splitted[0])-1].split('-')
    min = int(splitted[0][0])
    max = int(splitted[0][1])
    count = password.count(char)
    if count >= min and count <= max:
        correctfirst += 1
    if (password[min-1] == char) != (password[max-1] == char):
        correctsecond += 1

print(correctfirst)
print(correctsecond)