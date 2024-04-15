import heapq

def solution(n, paths, gates, param_summits):

    # 그래프 파싱
    graph = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])

    # 산봉오리 set으로
    summits = set(param_summits)
    
    # 초기화
    intensities = [float('inf')] * (n + 1)
    heap = []
    for gate in gates:
        intensities[gate] = 0
        heapq.heappush(heap, [0, gate])  # intensity_till, node
        
    # 다익스트라
    while heap:
        spent_time, current_node = heapq.heappop(heap)
        # 경계 조건: 1: 강도가 더 적은 경로가 저장되어 있음 or 2: 꼭대기인 경우 
        if intensities[current_node] < spent_time or current_node in summits :
            continue

        for next_node, consume_time in graph[current_node]:
            # intensity를 업그레이드 할 지 말지 고민.
            intensity_candidate = max(intensities[current_node], consume_time)
            # 다음 노드의 인텐시티가 더 인텐시티 후보보다 크다면, 이 경로가 더 인텐시티가 작은 경로 라는 것
            if intensities[next_node] > intensity_candidate:
                # 인텐시티 기록하기
                intensities[next_node] = intensity_candidate
                heapq.heappush(heap, [intensities[next_node], next_node])
                
    return list(min([(summit, intensities[summit]) for summit in param_summits], key=lambda x: (x[1], x[0])))