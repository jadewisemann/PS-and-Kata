"""
```yaml
problem: "디펜스 게임"
tags: 
difficulty: LV2
source: programmers
link: https://school.programmers.co.kr/learn/courses/30/lessons/142085
```
"""

from heapq import heappop, heappush

def solution(n, k, enemies):

    answer  = 0
    max_heap = []
    
    for enemy in enemies:
        
        heappush(max_heap, -enemy)
        n -= enemy
        
        if n < 0: 
            if k == 0: break
            k -= 1
            n -= heappop(max_heap)
        answer += 1
        
    return answer