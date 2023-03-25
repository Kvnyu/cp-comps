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

n = input()
nums = [int(num) for num in n]
out = [["." for _ in range(4)] for _ in range(4)]

for i in range(4):
    for j in range(4):
        if nums[i] & 1:
            out[j][i] = "*"
        nums[i] >>= 1

for line in out[::-1]:
    print(" ".join(line[0:2]) + "   " + " ".join(line[2:]))




