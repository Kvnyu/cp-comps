def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def ceildiv(a, b):
    return -(a // -b)

n, s = invr()
orders = [input() for _ in range(n)]
orders = [int(order) if len(order) == 1 else int(order[0]) + 1 for order in orders]
res = 0
water = s
for order in orders:
    if water < order:
        res += 1
        water = s
    water -= order
print(res)


