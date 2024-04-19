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

