from day6input import *

groups = input.split('\n\n')

count = 0 #1
groupanswers = [] #2

for group in groups:

    allananswers = set(list('abcdefghijklmnopqrstuvwxyz')) #2
    answers = set() #1

    people = group.split('\n')
    for person in people:

        allananswers = allananswers & set(list(person)) #2

        #1
        for answer in person:
            if answer not in answers:
                answers.add(answer)
                count = count + 1

    groupanswers.append(allananswers) #2

print(count) #1

#####2
answer2 = 0
for group in groupanswers:
    answer2 = answer2 + len(group)
print(answer2)