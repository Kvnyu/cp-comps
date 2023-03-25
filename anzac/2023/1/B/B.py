from sys import stdin, stdout
d, f = [x for x in stdin.readline().split()]
d = int(d)

res = None
for i, n in enumerate(f):
    if d > int(n):
        res = f[:i] + str(d) + f[i:]
        break

if res is None:
    res = f + str(d)


print(res)

