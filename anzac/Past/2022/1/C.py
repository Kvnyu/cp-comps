# integer inputs
def inp():
    return(int(input()))
# list inputs
def inlt():
    return(list(map(int,input().split())))
# input strings, returns a list of characters
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
# space separated integer variable inputs
def invr():
    return(map(int,input().split()))

# n, p, k = invr()
p = 972629409
k = 971799494
n = 191517

durations = [1 for _ in range(n)]
# print(res)
prefSum = [0]
for i in range(len(durations)*2):
    prefSum.append(prefSum[-1] + durations[i%n])


if p % prefSum[len(prefSum) // 2] == 0:
    print((p // prefSum[len(prefSum) // 2]) * k)
    quit()

# Note that whenever we have a player i start playing on a day, it will always end with another player j
# compute this end[i] = j array
# we can do it in n^2 time by searching linearly for each element, or nlog(n) using binary search
ends = [-1 for _ in range(n)]
target = p
# This binary search solution is too slow, need to use the two pointers solution
for start in range(n):
    lo = start
    hi = start + n - 1
    end = (lo + hi) // 2
    if sum(durations) < target:
        target = target % (sum(durations))
    while lo <= hi:
        end = (lo + hi) // 2
        amtTime = prefSum[end] - prefSum[start]

        if amtTime == target:
            lo = end
            hi = end
            break
        if amtTime < target:
            lo = end + 1
        else:
            hi = end - 1
    ends[start] = (hi) % n


# print(ends)

starter = 0
prev = -1
distanceToCycle = 0
firstSeen = {}
while starter not in firstSeen:
    distanceToCycle += 1
    prev = starter
    firstSeen[starter] = distanceToCycle
    # visit the end of the current start player + 1 to find the next starter
    # we want to stop when a starter is already visited, this will be the end of our cycle
    endPlayer = ends[starter]
    starter = (endPlayer) % n
distanceToCycle += 1

cycleEnd = prev
cycleStart = starter
res = 0
cycleRes = 0
i = 0 
cycleLen = 0
inCycle = 0
C = p // prefSum[len(prefSum) // 2] 
# cycleEnd = ends[cycleStart]
# print(cycleStart, cycleEnd)

# print(cycleEnd)
while k:
    # We manually reduce k up until we hit the cycle, once we're inside the cycle, we
    # figure out how many counts are in the cycleRes
    # If we reach the end of the cycle, we can try to eliminate the rest of k using the cycle
    k -= 1
    j = ends[i]
    count = C
    if j < i:
        count += 1
    if i == cycleStart:
        inCycle = 1
    if inCycle:
        cycleLen += 1
        cycleRes += count
    else:
        res += count

    if (i == cycleEnd):
        # print(cycleLen)
        rep = 1 + (k // cycleLen)
        res += cycleRes * rep
        k %= cycleLen
        cycleRes = 0

    i = j
print(res + cycleRes)

# we see starter again at distanceToCycle, so to find the length of a cycle we can do distanceToCycle - firstSeen[starter] 
# cycleLength = distanceToCycle - firstSeen[starter]
# You'll have one complete run per cycle
# How many runs do we have per cycle though ? 
# runThroughsPerCycle = 0

# curr = 0
# target = p
# runsToCycle = 0
# print(sum(durations), target)
# print(ends)
# triggered = False
# while True:
#     print("started on ", curr, " current run throughs ", runsToCycle)
#     if curr == starter:
#         if triggered:
#             break
#         else:
#             triggered = True
#     endPlayer = ends[curr]
#     if sum(durations) < target:
#         # print("hi")
#         runsToCycle += target // sum(durations)
#         target += prefSum[endPlayer + 1]
#     curr = (endPlayer + 1) % n
#     # print(curr, starter)

# print(runsToCycle)

# runsInACycle = 0
# curr = starter
# triggered = False
# while True:
#     print("started on ", curr, " current run throughs ", runsInACycle)
#     if curr == starter:
#         if triggered:
#             break
#         else:
#             triggered = True
#     endPlayer = ends[curr]
#     if sum(durations) < target:
#         # print("hi")
#         runsInACycle += target // sum(durations)
#         target += prefSum[endPlayer + 1]
#     curr = (endPlayer + 1) % n
#     # print(curr, starter)
# print(runsInACycle)



# This solution is O(k//n) which can be pretty bad if k is large and n is small 
# like p = 10**9 and n = 1
# res = 0
# i = 0 
# hoursLeft = p
# while k:
#     hoursLeft = p
#     while durations[i%n] <= hoursLeft:
#         hoursLeft -= durations[i%n]
#         if (i+1) % n == 0:
#             res += 1
#         i += 1
#     k -= 1