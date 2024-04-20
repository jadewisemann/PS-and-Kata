"""
```yaml
problem: "공 이동 시뮬레이션"
tags: 
difficulty: LV3
source: programmers
link: https://school.programmers.co.kr/learn/courses/30/lessons/87391 
```
"""

"""

n 행 m열

- 쿼리:
    - 0, dx : 열 번호 감소 방향 : down
    - 1, dx : 열 번호 증가 방향 : up
    - 2, dx : 행 번호 감소 방향 : <-
    - 3, dx : 행 번호 증가 방향 : ->

- 제한 사항
    - 공은 격자 밖으로 이동 불가.
    - 더 이상 이동 할 수없을때 멈춤

- 쿼리를 따라 이동했을 떄, x y 에 도착하는 점의 개수
    - n, m 10억, 완탐 절대 안됨
    - xy에서 역행해서 도달하는 점은 안되나?
    
"""

def solution(n, m, x, y, queries):
    
    row_back, row_front, col_back, col_front = x, x, y, y

    for commend, delta in queries[::-1]:
        
        if col_back > m - 1 or col_front < 0 or row_back > n - 1 or row_front < 0:
            return 0
        
        if commend == 0:
            col_front = min(col_front + delta , m - 1) 
            if col_back > 0:    
                col_back += delta

        elif commend == 1:
            col_back = max(0, col_back - delta)
            if col_front < m - 1:
                col_front -= delta

        elif commend == 2: 
            row_front = min(n-1, row_front + delta)
            if row_back > 0:
                row_back += delta

        elif commend == 3:
            row_back = max(0, row_back - delta)
            if row_front < n - 1:
                row_front -= delta

    return (col_front - col_back + 1) * (row_front - row_back + 1)