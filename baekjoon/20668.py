import heapq

# 세팅
SPEED_HI_LIMIT = 10
SPEED_LO_LIMIT = 1
LCM = 2520
# def solution(N, M, param_graph):
# 입력
I =  lambda: map(int, input().split())
N, M = I()
param_graph = [list(I())  for _ in range(M)]

# 그래프 파싱
graph = [[] for _ in range(N + 1)]
for  A,B,L,K in param_graph:
    ll = L * LCM
    graph[A].append((B,ll,K))
    graph[B].append((A,ll,K))

# 초기화.
times = [[float('inf')] * (SPEED_HI_LIMIT + 1) for _ in range (N + 1)]
times[1][1] = 0

Q = [(0,1,1)] # 시간, 정점, 속도


# 다익스트라
while Q:
    time, current_node, speed = heapq.heappop(Q)
    # 경계 조건: 시간이 더 적게 걸리는 경로 존재
    if times[current_node][speed] < time:
        continue
    
    for next_node, length, limit in graph[current_node]:
        # 경계 조건 : 속도 제한
        if speed <= limit:
            # 속도를 3가지 모두 큐에 넣기
            for dx in (-1, 0, +1):
                next_speed = speed + dx
                # 경계 조건,
                if not (SPEED_LO_LIMIT <= next_speed <= SPEED_HI_LIMIT):
                    continue
                next_time = time + (length // next_speed)
                if times[next_node][next_speed] > next_time:
                    times[next_node][next_speed] = next_time
                    heapq.heappush(Q, (next_time, next_node, next_speed))
                    
print(f"{(min(times[N])/LCM):.9f}") 
    
n, m = 3, 3
grp =[[1, 2, 2, 3],[2, 3, 6, 3],[1, 3, 7, 3]]

solution(n,m,grp)