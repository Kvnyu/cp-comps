n, k = input().split(" ")
n, k = int(n), int(k)

v1 = [int(x) for x in input().split(" ")][1:]
v2 = [int(x) for x in input().split(" ")][1:]

s1 = set()
for num in v1:
    s1.add(num)

s2 = set()
for num in v2:
    s2.add(num)

sRes = set()

for num in s1.union(s2):
    if (num in s1 and -num in s2) or (-num in s1 and num in s2):
        continue
    else:
        sRes.add(num)

if len(sRes) > 0:
    print(str(len(sRes)) + " " + " ".join(map(str, sorted(list(sRes), key=lambda x: abs(x)))))
else:
    print(0)


mRes = set()

for num in s1.union(s2):
    if num in s1 and num in s2:
        mRes.add(abs(num))
    elif num in s1 and -num in s2 or -num in s1 and num in s2:
        mRes.add(-(abs(num)))
    
if len(mRes) > 0:
    print(str(len(mRes)) + " " + " ".join(map(str, sorted(list(mRes), key=lambda x: abs(x)))) )
else:
    print(0)

def rotate(s, res):
    for num in s:
        newNum = (abs(num) - k) % n
        if newNum == 0:
            newNum = n
        newNum = -abs(newNum) if num <= 0 else abs(newNum)
        res.add(newNum)

rRes1 = set()
rRes2 = set()
rotate(s1, rRes1)
rotate(s2, rRes2)

if len(rRes1) > 0:
    print(str(len(rRes1)) + " " + " ".join(map(str, sorted(list(rRes1), key=lambda x: abs(x)))))
else:
    print(0)

if len(rRes2) > 0:
    print(str(len(rRes2)) + " " + " ".join(map(str, sorted(list(rRes2), key=lambda x: abs(x)))))
else:
    print(0)

