import heapq
def solution(operations):
    max_heap, min_heap = [],  []
    
    for operation in operations:
        operate , value = operation.split()

        # I, insert
        if operate.startswith("I"):
            element = int(value)
            heapq.heappush(min_heap,element)
            heapq.heappush(max_heap,((-1) * element))

        # D,  delete
        if operate.startswith("D"):
            if  not max_heap or not min_heap:
                continue
            
            # -1 || 1, min || max
            if value == "-1":
                delete_element = (-1) * heapq.heappop(min_heap)
                max_heap.remove(delete_element)
                heapq.heapify(max_heap)
            if value == "1":
                delete_element = (-1) * heapq.heappop(max_heap)
                min_heap.remove(delete_element)
                heapq.heapify(min_heap)
                
    return [0, 0] if not max_heap or not min_heap else [(-1)*(heapq.heappop(max_heap)),heapq.heappop(min_heap)] 
