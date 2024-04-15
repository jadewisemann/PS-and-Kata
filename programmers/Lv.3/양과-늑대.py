#! 양과 늑대

# 시작점은 루트 노드 , 0번
# 다시 0번으로 돌아오는 경로를 그리는 것

# 양을 지나면, 양이 쌓인다
# 늑대를 지나면 늑대가 쌓인다.
# 늑대가 양보다 같거나 많아지는 순간, 먹힌다.

# 루트노드로 다시 순회하면서 모을 수있는 양이 최대 몇마리인지 구하자


# ! param

# info, 2-17, info의 i번 노드에 있는 양 또는 늑대의를 나타낸다.
# 0은 양 1은 늑대
# 루트 노드, info [0] 은 항상 0임이 보장된다.

# edges, 세로행의 길이, info - 1
# 리스트 인 리스트
# 원소들은 길이가 2인 리스트
# 원소 둘의 연결 관계를 나타낸다.
# [부모, 자식]
# !풀이

# 루트 노드에서 bfs 하면 될 것 같은데?

def solution(info, edges):
    # try 1, bfs

    # declare global
    results = []
    visited = []
    
    # parse edges => make tree
    tree = {node:[] for node in range(len(info))}
    for parent, child in edges:
        tree[parent].append(child)

    # tree 순회
    Q = [[0, 0, [0]]] # wolves, sheep, path
    while Q:
        wolves, sheep, path = Q.pop(0) 
        current_node = path[-1]
        visited.append(current_node)
        
        # 늑대 인지 양인지 확인
        if info[current_node]:
            wolves += 1
        else:
            sheep += 1

        # check wolves or loop end 
        if wolves >= sheep  or current_node == 0 and not len(path) == 1 :
            results.append(sheep)
            continue
        
        # 연결 관계 확인
        for next_node in tree[current_node]:
            # 예외, 방문
            if next_node in visited:
                continue
            Q.append([wolves, sheep, [*path,next_node]])
    return