pk1 = 10943862
pk2 = 12721030


def findLoopSize(subjectNr, pk):
    value = 1
    loopsize = 0
    while value != pk:
        value = value * subjectNr
        value = value % 20201227
        loopsize += 1
    return loopsize

def transform(pk, loopsize):
    value = 1
    for _ in range(0,loopsize):
        value = value * pk
        value = value % 20201227
    return value

loopCard = findLoopSize(7, pk1)
loopDoor = findLoopSize(7, pk2)

#print(loopCard)
#print(loopDoor)

ek1 = transform(pk1, loopDoor)
ek2 = transform(pk2, loopCard)
if ek1 == ek2:
    print(ek2)