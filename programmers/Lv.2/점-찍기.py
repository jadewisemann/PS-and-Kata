"""
```yaml
problem: "점 찍기"
tags: 
difficulty: LV2
source: programmers
link: https://school.programmers.co.kr/learn/courses/30/lessons/140107
```
"""

def solution(k, d):
    count = 0
    for a in range(0, d//k + 1):
        count += 1 + int(((d ** 2) - (a * k) ** 2) ** 0.5) // k
    return count
