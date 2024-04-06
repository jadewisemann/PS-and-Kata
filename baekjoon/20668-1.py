import heapq

def dijkstra(graph, N):
    lcm = 2520
    min_time = [float('inf')] * (N * 11)
    min_time[1] = 0
    Q = [(0, 1, 1)]  # 시간, 노드, 속도

    while Q:
        current_time, current_node, current_speed = heapq.heappop(Q)
        current_index = current_node + N * (current_speed - 1)

        if min_time[current_index] < current_time:
            continue

        for next_node, length, speed_limit in graph[current_node]:
            for next_speed in [current_speed - 1, current_speed, current_speed + 1]:
                if 1 <= next_speed <= speed_limit:
                    next_time = current_time + (length / next_speed) * lcm
                    next_index = next_node + N * (next_speed - 1)
                    if next_time < min_time[next_index]:
                        min_time[next_index] = next_time
                        heapq.heappush(Q, (next_time, next_node, next_speed))

    
    return min(min_time[N * speed:N * (speed+1)] for speed in range(1, 11)) / lcm

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, L, K = map(int, input().split())
    graph[A].append((B, L, K))
    graph[B].append((A, L, K))

result = dijkstra(graph, N)
print(f"{result:.9f}")

