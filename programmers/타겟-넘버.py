def solution(numbers, target):
    Q = [0]
    for number in numbers:
        tQ = []
        while Q:
            acc = Q.pop()
            tQ.append(acc+number)
            tQ.append(acc-number)    
        Q = tQ
            
    return Q.count(target) or 0 