correct = int(input())
myAns = input()
hisAns = input()
matching = 0
for i in range(len(myAns)):
    if myAns[i] == hisAns[i]:
        matching += 1

total = len(myAns)
matchingCorrect = 0
if matching > correct:
    matchingCorrect = correct
else:
    matchingCorrect = matching
remainingCorrect = total - max(matching, correct)
print(matchingCorrect + remainingCorrect)




