"""
```yaml
problem: '두 원 사이의 정수 쌍'
tags: 
difficulty: Lv.2
source: programmers
link: https://school.programmers.co.kr/learn/courses/30/lessons/181187
```
"""

from math import floor, ceil

def solution(r1, r2):
    count = 0
    for curr_y in range(r2+1):
        max_x = floor((r2**2 - curr_y**2)**0.5)
        min_x = ceil((r1**2 - curr_y**2)**0.5) if r1 > curr_y else 0
        add_val = ((max_x - min_x +1) * 2 - (0 if min_x else 1))
        count += add_val * (2 if curr_y else 1)        
    return(count)