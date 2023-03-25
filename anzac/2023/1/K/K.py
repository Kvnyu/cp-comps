num = int(input())

ranges = [[int(x) for x in input().split(" ")] for _ in range(num)]
items = []
for start, end in ranges:
    items.append(start)
    items.append(end)

m = -1
for i in range(1, num+1):
    mustBeTruth = 0
    for start, end in ranges:
        if start <= i <= end:
            mustBeTruth += 1
    if mustBeTruth == i:
        m = max(m, i)
print(m)

