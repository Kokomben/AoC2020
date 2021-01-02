from day5input import *

input = input.split('\n')
input = input[1:len(input)-1]

def roundUp(a):
    return int(a) + 1 if a != float( int(a) ) else int(a)

def process(items, r):
    answer = r[ : int( len(r) / 2 ) ] if items[0] == 'F' or items[0] == 'L' else r[ roundUp( len(r) / 2 ) : ]
    return process(items[1:], answer) if len(list(answer)) > 0 else answer.start

ids = []
for p in input:
    row = process(p[:-3], range(0,127))
    column = process(p[-3:], range(0,7))
    ids.append(row*8+column)

answer1 = max(ids)
print(answer1)

myId = 0
for nr in range(1,answer1):
    if nr - 1 in ids and nr + 1 in ids and nr not in ids:
        myId = nr
print(myId)
        
        
