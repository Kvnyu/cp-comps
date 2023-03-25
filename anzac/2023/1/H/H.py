from collections import Counter
n, s = input().split(" ")
n, s = int(n), int(s)
matrix = [input() for _ in range(n)]

# do prefix sum per row in matrix
prefHorizontal = [[0 for _ in range(n+1)] for _ in range(n)]
for i in range(n):
    for j in range(1, n+1):
        if matrix[i][j-1] == "D":
            if j == 1:
                prefHorizontal[i][j] = 1
            else:
                prefHorizontal[i][j] = prefHorizontal[i][j-1] + 1
        else:
            if j == 1:
                prefHorizontal[i][j] = 0
            else:
                prefHorizontal[i][j] = prefHorizontal[i][j-1]

prefVertical = [[0 for _ in range(n)] for _ in range(n+1)]
for j in range(n):
    for i in range(1, n+1):
        if matrix[i-1][j] == "D":
            if i == 1:
                prefVertical[i][j] = 1
            else:
                prefVertical[i][j] = prefVertical[i-1][j] + 1
        else:
            if i == 1:
                prefVertical[i][j] = 0
            else:
                prefVertical[i][j] = prefVertical[i-1][j]

def dirty_horizontal_squares_between(p1, p2):
    return prefHorizontal[p2[0]][p2[1]] - prefHorizontal[p1[0]][p1[1]]

def dirty_veritcal_squares_between(p1, p2):
    a = prefVertical[p2[0]][p2[1]]
    b = prefVertical[p1[0]][p1[1]]
    return a - b

# # begins at (0,0)
# square1 = 0
# for i in range(s):
#     square1 += dirty_horizontal_squares_between((i,0), (i,s))

# # begins at (1,0)
# square2 = square1 + dirty_horizontal_squares_between((s, 0), (s, s)) - dirty_horizontal_squares_between((0,0), (0,s))

# # begins at (1,1)
# square3 = square2 - dirty_veritcal_squares_between((1,0), (1+s, 0)) + dirty_veritcal_squares_between((1, 1+s), (1+s, 1+s))

arr = [[0 for _ in range(n-s+1)] for _ in range(n-s+1)]
d = Counter()

for i in range(n-s+1):
    for j in range(n-s+1):
        if i == 0 and j == 0:
            square1 = 0
            for k in range(s):
                square1 += dirty_horizontal_squares_between((k,0), (k, s))
            arr[i][j] = square1
        else:
            if j == 0:
                arr[i][j] = arr[i-1][j] - dirty_horizontal_squares_between((i-1,j), (i-1, j+s))  + dirty_horizontal_squares_between((i+s-1, j), (i+s-1, j+s))
            else:
                arr[i][j] = arr[i][j-1] - dirty_veritcal_squares_between((i, j-1), (i+s, j-1)) + dirty_veritcal_squares_between((i, j+s-1), (i+s, j+s-1))
        d[arr[i][j]] += 1

dirtySpots = sorted(list(d.keys()))
for dirtySpot in dirtySpots:
    print(f'{dirtySpot} {d[dirtySpot]}')
