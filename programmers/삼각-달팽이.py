from itertools import chain, cycle

def solution(n):
    triangle = [[0] * i for i in range(1, n + 1)]
    x, y = 0,0
    current_number = 1
    directions = [[+1, 0], [0, +1], [-1,-1]]
    moves = list(chain(*[[direction] * idx for idx, direction in zip(range(n, 0, -1), cycle(directions))]))
    for dx, dy in moves[1:]:
        x += dx
        y += dy
        triangle[x][y] = current_number
        current_number += 1
    return  list(chain(*triangle))

