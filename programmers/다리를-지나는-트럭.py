# !! 문제
# 모든 트럭이 다리를 건더는데 걸리는 시간 구하기
# !! 매개변수
# bridge_length: 이 길이 만큼의 트럭이 한번에 올라 올 수 있음
# weight: 이 만큼의 무게를 견딜 수 있음
# truck_weight: 트럭들의 무개가 담긴 배열, 순서가 있음
# !! 분석
# 다리를 지나는 데에는 길이 만큼의 초가 걸림

def solution(bridge_length, weight, truck_weights):
    tmp = []
    result = 0
    for truck in truck_weights:
        if not tmp:
            tmp.append(truck)
            continue
        else:
            if (sum(tmp) + truck) <= weight and len(tmp) <= bridge_length :
                tmp.append(truck)
            else:
                result += bridge_length + len(tmp) - 1
                tmp = [truck]
    else: result += bridge_length + len(tmp) - 1
    return result + 1

print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
# 7. 2 
# 4, 2
# 5, 2
# 6, 2
# 각.(2) 합.(2)+1*(n-1) 각.(2) / +1  = 8
# 합 (100)+ 1* (n-1 = 9) + 1 = 110

