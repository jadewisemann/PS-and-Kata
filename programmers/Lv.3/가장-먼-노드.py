"""
```yaml
problem: '가장 먼 노드'
tags: 그래프
difficulty: Lv.3
source: programmers
link: https://school.programmers.co.kr/learn/courses/30/lessons/49189
```
"""


from collections import deque

NOT_VISIT = -1

def solution(n, edges):
    
    graph = [[] for _ in range(n+1)]

    for n1, n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    distances = [NOT_VISIT] * (n+1)
    
    distances[1] = 0
    queue = deque([1])
    
    while queue:
        current = queue.popleft()
        for next_node in graph[current]:
            if distances[next_node] == -1 :
                distances[next_node] = distances[current] + 1
                queue.append(next_node)
                
    return distances.count(max(distances))
