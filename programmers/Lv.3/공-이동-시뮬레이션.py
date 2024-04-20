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
    - 공은 격자 밖으로ㅓ 이동 불가.
    - 더 이상 이동 할 수없을때 멈춤

- 쿼리를 따라 이동했을 떄, x y 에 도착하는 점의 개수
    - n, m 10억, 완탐 절대 안됨
    - xy에서 역행해서 도달하는 점은 안되나?
    
[[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]	
"""

def solution(n, m, x, y, queries):
    
    row_min, row_max, col_min, col_max = x,x,y, y

    for commend, delta in queries[::-1]:
        
        if col_min > m - 1 or col_max < 0 or row_min > n - 1 or row_max < 0:
            return 0
        
        if commend == 0:
            col_max = min(col_max + delta , m - 1) 
            if col_min > 0:    
                col_min += delta

        elif commend == 1:
            col_min = max(0, col_min - delta)
            if col_max < m - 1:
                col_max -= delta

        elif commend == 2: 
            row_max = min(n-1, row_max + delta)
            if row_min > 0:
                row_min += delta

        elif commend == 3:
            row_min = max(0, row_min - delta)
            if row_max < n - 1:
                row_max -= delta

    return (col_max - col_min + 1) * (row_max - row_min + 1)