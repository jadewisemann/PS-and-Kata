"""
```yaml
problem: "우박수열 정적분"
tags:
difficulty: LV2
source: programmers
link: https://school.programmers.co.kr/learn/courses/30/lessons/134239
```
"""

def collatz_conjecture(target_number):
    result = [target_number]
    while target_number > 1:
        if  target_number % 2 == 0:
            target_number //= 2
        else:  
            target_number *= 3
            target_number += 1
            
        result.append(target_number)
        
    return result

def definite_integral(list, range):
    N = len(list)
    s, t = range 
    # 구간 체크
    if (s > N + t) or (t > s): 
        return -1.0
    t_list = list[s:t] + [list[t]]
    return sum(t_list) - (((t_list[0]+ t_list[-1]) / 2) if t_list else 0)

def solution(k, ranges):
    collatz_list = collatz_conjecture(k)
    results = []
    for range in ranges:
        # parse range
        s, e = range
        results.append(definite_integral(collatz_list,[s,(e if e > 0 else e-1)]))
    return results
