def ceildiv(a, b):
    return -(a // -b)

x, y = [int(x) for x in input().split(" ")]
sols = [int(x) for x in input().split(" ")]

m = max(sols)
print(ceildiv(m * y, 1000))