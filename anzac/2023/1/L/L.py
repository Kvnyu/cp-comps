from math import sqrt
arr = [int(x) for x in input().split(" ")]

px, py = arr[0], arr[1]
x1, y1 = arr[2], arr[3]
x2, y2 = arr[4], arr[5]

if x1 <= px <= x2:
    output = min(abs(py - y1), abs(py - y2))

elif y1 <= py <= y2:
    output = min(abs(px - x1), abs(px - x2))

else:
    def dist(point1, point2):
        return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    point1 = (px, py)
    point2 = (x1, y1)
    point3 = (x1, y2)
    point4 = (x2, y1)
    point5 = (x2, y2)
    output = min(dist(point1, point2), dist(point1, point3), dist(point1, point4), dist(point1, point5))


print("{0:.3f}".format(output))