r, y = [int(x) for x in input().split(" ")]
matrix = [[int(x) for x in input().split(" ")] for _ in range(r)]

output = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
for i in range(1, len(matrix)-1):
    for j in range(1, len(matrix[0]) - 1):
        val = matrix[i][j]
        if matrix[i-1][j] > val and matrix[i+1][j] > val and matrix[i][j-1] > val and matrix[i][j+1] > val:
            output[i][j] = 1

for line in output:
    print(" ".join(map(str, line)))
        

