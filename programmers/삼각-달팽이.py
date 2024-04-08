from itertools import chain, cycle
def solution(n):
    triangle, x, y, current_number = [[0] * i for i in range(1, n + 1)], -1 , 0 , 1
    for dx, dy in list(chain(*[[direction] * idx for idx, direction in zip(range(n, 0, -1), cycle([[+1, 0], [0, +1], [-1,-1]]))])):
        x, y = x+dx, y+dy
        triangle[x][y] = current_number
        current_number += 1
    return  list(chain(*triangle))

