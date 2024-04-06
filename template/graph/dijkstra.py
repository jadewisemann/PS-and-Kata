import heapq
push = heapq.heappush
pop = heapq.heappop

INF = 10 ** 8

def dijkstra(graph, start):
    distances = {node: (0 if start else INF) for node in graph}
    queue = [[0, start]]
    
    while queue:
        current_distance, current_node = pop(queue) 
        
        # 저장된 경로가 더 짧은면 넘어감
        if distances[current_node] < current_distance:
            continue

        # 현재 노드의 다음 노드와의 연결 관계를 순회
        for next_node, weight in graph[current_node].items():
            # 거리는  지금까지의 거리 + 가중치
            distance = current_distance + weight
            
            # 현재 노드를 거치는 것이 새로운 최단 경로인 경우
            if distance < distances[next_node]:
                distances[next_node] = distance
                
                push(queue, [distance, next_node])  # 우선순위 큐에 추가

    return distances

# 그래프 예시
graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

# 'A'에서 시작하여 각 노드까지의 최단 거리 출력
print(dijkstra(graph, 'A'))