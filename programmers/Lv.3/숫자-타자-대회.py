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
    
    def calc_weight(dial_dict,pos_start, pos_end):    
        [xa, ya], [xb,yb] = dial_dict[pos_start], dial_dict[pos_end] 
        dx, dy = abs(xa-xb), abs(ya - yb)
        return 1 if not (dx or dy) else ((dx+dy) + max(dx, dy))

    dial_dict = {
        el: [idx, jdx]
            for idx, list in enumerate(DIAL_LISTS)
            for jdx, el in enumerate(list)
    }
    
    every_number = list(num for num in range(10))

    pre_calc_weight = []
    for left in (every_number): 
        tmp_list = []
        for right in every_number:
            tmp_list.append(calc_weight(dial_dict, left, right))
        pre_calc_weight.append(tuple(tmp_list))
    return tuple(pre_calc_weight)


def solution( numbers ): 
    
    INF = float( 'inf' )
    WEIGHTS = pre_calc_weight()
    queue = { (START_POSITION['left'], START_POSITION['right']): 0 }
    
    for curr_number in list(map(int, numbers)):
        next_queue = {}
        for (left_pos, right_pos), weight_sum in queue.items():
            if left_pos == curr_number or right_pos == curr_number:
                next_queue[ (left_pos, right_pos) ] = min(
                    next_queue.get( (left_pos, right_pos), INF ), 
                    weight_sum+1
                )
                continue

            next_queue[(left_pos, curr_number)] = min(
                next_queue.get( (left_pos, curr_number), INF ), 
                weight_sum + WEIGHTS[right_pos][curr_number]
            )

            next_queue[ (curr_number, right_pos) ] = min(
                next_queue.get( (curr_number, right_pos), INF ), 
                weight_sum + WEIGHTS[left_pos][curr_number]
            )
            
        queue = next_queue

    return min(queue.values())