import sys
import heapq

input = lambda: sys.stdin.readline().strip()

# 입력
coordinates = [] 
for _ in range(int(input())):
    coordinates.append(sorted(list(map(int, input().split(" ")))))

length = int(input())

# 정렬
coordinates.sort(key=lambda x: (x[1], x[0]))

# 순회
heap = []
global_max = 0

for coordinate in coordinates:
    head, tail = coordinate
    heapq.heappush(heap, head)
    start = tail - length 
    while heap and heap[0] < start: 
        heapq.heappop(heap) 
    global_max = max(global_max, len(heap))

print(global_max)