"""
```yaml
problem: "숫자 타자 대회"
tags: 
difficulty: LV3
source: programmers
link: https://school.programmers.co.kr/learn/courses/30/lessons/136797
```
"""


DIAL_LISTS = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ["*",0,"#"]
]

START_POSITION = {
    'left' : 4,
    'right' : 6
}



def pre_calc_weight():
    def parse_lists_to_dict (lists):
        
        dict = {}
        N = len(lists)
        for idx in range(N):
            for jdx in range(N):
                dict[lists[idx][jdx]] = [idx,jds]
                
        for idx, list in enumerate(lists):
            for jdx, el in enumerate(list):
                dict[el] = [idx,jdx]
        return dict

    def calc_weight(dial_dict,pos_start, pos_end):    
        [xa, ya], [xb,yb] = dial_dict[pos_start], dial_dict[pos_end] 
        dx, dy = abs(xa-xb), abs(ya - yb)
        return 1 if not (dx or dy) else (0 if  not ( dx or dy ) else  dx + dy + ( dx if dx > dy else dy ))

    dial_dict = parse_lists_to_dict(DIAL_LISTS)
    every_number = list(num for num in range(10))

    pre_calc_weight = []
    for left in (every_number): 
        tmp_list = []
        for right in every_number:
            tmp_list.append(calc_weight(dial_dict, left,right))
        pre_calc_weight.append(tuple(tmp_list))
    pre_calc_weight = tuple(pre_calc_weight)
    return pre_calc_weight


def solution(numbers): 
    
    INF = float('inf')
    WEIGHT_RST = pre_calc_weight()

    
    
    queue = {
        (START_POSITION['left'],START_POSITION['right']):0,
        (START_POSITION['right'],START_POSITION['left']):0
    }
    
    for number in [int(char) for char in numbers]:

        next_queue = {}
        
        for (left_pos, right_pos), weight_sum in queue.items():

            if (( left_pos == number ) or ( right_pos == number )):
                next_queue[(left_pos, right_pos)] = (
                next_queue[(right_pos, left_pos)] ) = (
                min( 
                    next_queue.get(( left_pos, right_pos ), INF ),
                    weight_sum + 1
                ))
                
            else:
                next_queue[(left_pos, number)] = (
                next_queue[(number, left_pos)] ) = (
                min(
                    next_queue.get((left_pos, number), INF),
                    weight_sum + WEIGHT_RST[right_pos][number]
                ))
                
                next_queue[(right_pos, number)] = (
                next_queue[(number, right_pos)] ) = (
                min(
                    next_queue.get((right_pos, number), INF),
                    weight_sum + WEIGHT_RST[left_pos][number]
                ))

        queue = next_queue

    return min(queue.values())



""" find when it needed
테스트 1 〉	    통과 (0.04ms, 10.4MB)
테스트 2 〉	    통과 (0.03ms, 10.4MB)
테스트 3 〉	    통과 (0.04ms, 10.4MB)
테스트 4 〉	    통과 (0.06ms, 10.6MB)
테스트 5 〉	    통과 (0.12ms, 10.4MB)
테스트 6 〉	    통과 (0.14ms, 10.3MB)
테스트 7 〉	    통과 (0.12ms, 10.4MB)
테스트 8 〉	    통과 (0.14ms, 10.4MB)
테스트 9 〉	    통과 (0.07ms, 10.2MB)
테스트 10 〉	통과 (0.14ms, 10.4MB)
테스트 11 〉	통과 (0.75ms, 10.4MB)
테스트 12 〉	통과 (0.75ms, 10.4MB)
테스트 13 〉	통과 (0.68ms, 10.3MB)
테스트 14 〉	통과 (0.70ms, 10.3MB)
테스트 15 〉	통과 (0.38ms, 10.4MB)
테스트 16 〉	통과 (1225.35ms, 10.5MB)
테스트 17 〉	통과 (1316.43ms, 10.7MB)
테스트 18 〉	통과 (1640.62ms, 10.9MB)
테스트 19 〉	통과 (2629.75ms, 11.1MB)
테스트 20 〉	통과 (4167.05ms, 11.2MB) 
"""

""" pre calculate all the weight before
테스트 1 〉 	통과 (0.07ms, 10.4MB)
테스트 2 〉 	통과 (0.10ms, 10.5MB)
테스트 3 〉 	통과 (0.12ms, 10.4MB)
테스트 4 〉 	통과 (0.10ms, 10.4MB)
테스트 5 〉 	통과 (0.16ms, 10.4MB)
테스트 6 〉 	통과 (0.20ms, 10.3MB)
테스트 7 〉 	통과 (0.16ms, 10.4MB)
테스트 8 〉 	통과 (0.16ms, 10.4MB)
테스트 9 〉 	통과 (0.18ms, 10.6MB)
테스트 10 〉	통과 (0.18ms, 10.4MB)
테스트 11 〉	통과 (0.51ms, 10.4MB)
테스트 12 〉	통과 (0.30ms, 10.4MB)
테스트 13 〉	통과 (0.48ms, 10.5MB)
테스트 14 〉	통과 (0.44ms, 10.4MB)
테스트 15 〉	통과 (0.34ms, 10.3MB)
테스트 16 〉	통과 (632.24ms, 10.5MB)
테스트 17 〉	통과 (602.14ms, 10.7MB)
테스트 18 〉	통과 (1002.37ms, 10.7MB)
테스트 19 〉	통과 (1657.06ms, 10.9MB)
테스트 20 〉	통과 (2585.45ms, 11.1MB)
"""