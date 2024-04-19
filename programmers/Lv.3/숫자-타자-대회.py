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
    pre_calc_weight = tuple(pre_calc_weight)
    return pre_calc_weight


def solution( numbers ): 
    
    INF = float( 'inf' )
    WEIGHTS = pre_calc_weight()

    queue = { (START_POSITION['left'], START_POSITION['right']): 0 }
    
    for number in [int(char) for char in numbers]:
        
        next_queue = {}
        
        for ( left_pos, right_pos ), weight_sum in queue.items():

            if ( (left_pos == number) or (right_pos == number) ):
                next_queue[ (left_pos, right_pos) ] = ( min( 
                    next_queue.get(( left_pos, right_pos ), INF ),
                    weight_sum + 1
                ))
                continue
            
            next_queue[(left_pos, number)] = ( min(
                next_queue.get((left_pos, number), INF),
                weight_sum + WEIGHTS[right_pos][number]
            ))
            
            next_queue[(right_pos, number)] = ( min(
                next_queue.get((right_pos, number), INF),
                weight_sum + WEIGHTS[left_pos][number]
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

""" refactoring, make function nested, decrease function overhead

테스트 1 〉 	통과 (0.07ms, 10.5MB)
테스트 2 〉 	통과 (0.07ms, 10.4MB)
테스트 3 〉 	통과 (0.07ms, 10.5MB)
테스트 4 〉 	통과 (0.08ms, 10.5MB)
테스트 5 〉 	통과 (0.09ms, 10.5MB)
테스트 6 〉 	통과 (0.12ms, 10.2MB)
테스트 7 〉 	통과 (0.10ms, 10.5MB)
테스트 8 〉 	통과 (0.17ms, 10.5MB)
테스트 9 〉 	통과 (0.10ms, 10.5MB)
테스트 10 〉	통과 (0.10ms, 10.4MB)
테스트 11 〉	통과 (0.28ms, 10.4MB)
테스트 12 〉	통과 (0.28ms, 10.5MB)
테스트 13 〉	통과 (0.26ms, 10.5MB)
테스트 14 〉	통과 (0.28ms, 10.6MB)
테스트 15 〉	통과 (0.20ms, 10.4MB)
테스트 16 〉	통과 (342.66ms, 10.5MB)
테스트 17 〉	통과 (562.07ms, 10.5MB)
테스트 18 〉	통과 (794.29ms, 10.9MB)
테스트 19 〉	통과 (1202.50ms, 11.1MB)
테스트 20 〉	통과 (1676.37ms, 11.2MB)
"""

""" search one index
테스트 1 〉	    통과 (0.08ms, 10.5MB)
테스트 2 〉	    통과 (0.08ms, 10.5MB)
테스트 3 〉	    통과 (0.14ms, 10.4MB)
테스트 4 〉	    통과 (0.14ms, 10.3MB)
테스트 5 〉	    통과 (0.09ms, 10.5MB)
테스트 6 〉	    통과 (0.10ms, 10.5MB)
테스트 7 〉	    통과 (0.09ms, 10.5MB)
테스트 8 〉	    통과 (0.09ms, 10.3MB)
테스트 9 〉	    통과 (0.10ms, 10.4MB)
테스트 10 〉	통과 (0.09ms, 10.4MB)
테스트 11 〉	통과 (0.18ms, 10.4MB)
테스트 12 〉	통과 (0.17ms, 10.4MB)
테스트 13 〉	통과 (0.17ms, 10.5MB)
테스트 14 〉	통과 (0.30ms, 10.6MB)
테스트 15 〉	통과 (0.14ms, 10.4MB)
테스트 16 〉	통과 (164.12ms, 10.5MB)
테스트 17 〉	통과 (257.01ms, 10.7MB)
테스트 18 〉	통과 (410.10ms, 10.9MB)
테스트 19 〉	통과 (550.77ms, 11.2MB)
테스트 20 〉	통과 (757.04ms, 11.1MB)
"""