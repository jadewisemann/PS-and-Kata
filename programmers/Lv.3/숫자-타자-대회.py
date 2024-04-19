"""

```yaml
problem: "숫자 타자 대회"
tags: 
difficulty: LV3
source: programmers
link: https://school.programmers.co.kr/learn/courses/30/lessons/136797
```

"""

def solution(numbers):
    answer = 0
    return answerDIAL_LISTS = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ["*",0,"#"]
]


START_POSITION = {
    'left' : 4,
    'right' : 6
}

    

def parse_lists_to_dict (lists):
    
    dict = {}
    for idx, list in enumerate(lists):
        for jdx, el in enumerate(list):
            # is element verification logic needed?
            dict[el] = [idx,jdx]
    return dict

def calc_weight(pos_start, pos_end):    
    [xa, ya], [xb,yb] = dial_dict[pos_start], dial_dict[pos_end] 
    dx, dy = abs(xa-xb), abs(ya - yb)
    return 1 if not (dx or dy) else (0 if  not ( dx or dy ) else  dx + dy + ( dx if dx > dy else dy ))

def solution(numbers): 
    
    global dial_dict
    dial_dict = parse_lists_to_dict(DIAL_LISTS)

    
    memory = {
        (START_POSITION['left'],START_POSITION['right']):0,
        (START_POSITION['right'],START_POSITION['left']):0
    }
    
    
    # 숫자 순회

    for number in [int(char) for char in numbers]:
        
        new_memory = {}
        
        for (left_pos, right_pos), weight_sum in memory.items():

            if left_pos == number or right_pos == number:
                new_memory[(left_pos, right_pos)] = new_memory[(right_pos, left_pos)] = min(new_memory.get((left_pos, right_pos), float('inf')), weight_sum + 1)

            else:
                new_memory[(left_pos, number)] = new_memory[(number, left_pos)] = min(new_memory.get((left_pos, number), float('inf')), weight_sum + calc_weight(right_pos, number))
                new_memory[(right_pos, number)] = new_memory[(number, right_pos)] = min(new_memory.get((right_pos, number), float('inf')), weight_sum + calc_weight(left_pos, number))

        memory = new_memory

    return min(memory.values())



""" find when it needed
테스트 1 〉	통과 (0.04ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (0.06ms, 10.6MB)
테스트 5 〉	통과 (0.12ms, 10.4MB)
테스트 6 〉	통과 (0.14ms, 10.3MB)
테스트 7 〉	통과 (0.12ms, 10.4MB)
테스트 8 〉	통과 (0.14ms, 10.4MB)
테스트 9 〉	통과 (0.07ms, 10.2MB)
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