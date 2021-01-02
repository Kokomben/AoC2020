inputString = """Player 1:
29
30
44
35
27
2
4
38
45
33
50
21
17
11
25
40
5
43
41
24
12
19
23
8
42

Player 2:
32
13
22
7
31
16
37
6
10
20
47
46
34
39
1
26
49
9
48
36
14
15
3
18
28"""

playersString = inputString.split("\n\n")
d1 = [int(x) for x in playersString[0].split("\n")[1:]]
d2 = [int(x) for x in playersString[1].split("\n")[1:]]

def round(deck1, deck2):
    card1 = deck1[0]
    del deck1[0]
    card2 = deck2[0]
    del deck2[0]

    if card1 > card2:
        deck1 += [card1, card2]
    else:
        deck2 += [card2, card1]
    return [deck1, deck2]

def part1(deck1, deck2):
    count = 0
    while len(deck1) > 0 and len(deck2) > 0:
        result = round(deck1, deck2)
        deck1 = result[0]
        deck2 = result[1]
        count += 1

    #print(count)
    winnerdeck = deck1 if len(deck1) > len(deck2) else deck2
    #print(winnerdeck)
    score = calculateScore(winnerdeck)
    print(score)

def calculateScore(deck):
    value = len(deck)
    score = 0
    for card in deck:
        score = score + card*value
        value -= 1
    return score

part1(d1.copy(),d2.copy())

###Part2
def playGame(deck1, deck2):
    mem1 = set()
    mem2 = set()
    while len(deck1) > 0 and len(deck2) > 0:
        futuremem1 = tuple(deck1.copy())
        futuremem2 = tuple(deck2.copy())

        if futuremem1 in mem1 and futuremem2 in mem2:
            return [1, deck1, deck2]

        card1 = deck1[0]
        del deck1[0]
        card2 = deck2[0]
        del deck2[0]
        
        if card1 <= len(deck1) and card2 <= len(deck2):
            roundWinner = playGame(deck1.copy()[0:card1], deck2.copy()[0:card2])[0]
        else:
            roundWinner = 1 if card1 > card2 else 2

        if roundWinner == 1:
            deck1 += [card1, card2]
        else:
            deck2 += [card2, card1]

        mem1.add(futuremem1)
        mem2.add(futuremem2)

    return [1 if len(deck2) == 0 else 2, deck1, deck2]

result = playGame(d1, d2)
winnerScore = calculateScore(result[1]) if result[0] == 1 else calculateScore(result[2])
print(winnerScore)