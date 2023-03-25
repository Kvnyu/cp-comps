fib = [0, 1, 1, 2, 3, 5, 8]
n = int(input())
out = []
for i in range(1, n+1):
    if i in fib:
        out.append("fizz")
    else:
        out.append("buzz")

print("".join(out))
