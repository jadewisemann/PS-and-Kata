def solution(maps):
    # 변수 선언
    col, low = len(maps), len(maps[0])
    visited = [[False] * low for _ in range(col)]

    foods = []

    # 지도 순회
    for jdx in range(col):
        for idx in range(low):
            # X 거나 방문했으면 건너 뛰기
            if maps[jdx][idx] == "X" or visited[jdx][idx]:
                continue
                
            # 변수 초기화
            food = 0  
            queue = [(idx, jdx)]
            # 큐가 빌 때까지 = 한 섬을 전부 탐색
            while queue:
                ox, oy = queue.pop(0)
                if visited[oy][ox]:
                    continue
                visited[oy][ox] = True
                food += int(maps[oy][ox])
                # 상하 좌우 이동
                for dx, dy in [(-1,0), (1, 0), (0, 1), (0, -1)]:
                    nx, ny = ox + dx, oy + dy
                    # 경계 조건: 
                    if (
                        0 <= nx < low and 0 <= ny < col  # nx, ny는 범위 내
                        and maps[ny][nx] != "X"  # 방문 하고자 하는 좌표가 X가 아님
                        and not visited[ny][nx]  # 방문 한적이 없으면
                    ): queue.append((nx, ny))

            # 순회가 끝, 배열에 더하기 
            foods.append(food)
    
    # 탐색된 섬이 없다면 [-1] 반환, 있으면 크기 순으로 정렬하여 반환
    return sorted(foods) if foods else [-1]
