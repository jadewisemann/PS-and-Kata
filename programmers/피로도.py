from itertools import permutations, combinations

def solution(initial_fatigue, param_dungeons):
    max_counter = 0
    dungeons = list(filter(lambda x: x[0] <= initial_fatigue, param_dungeons))
    paths = permutations(dungeons)
    for path in paths:
        if max_counter == len(dungeons):
            break
        current_fatigue = initial_fatigue
        dungeon_clear_counter = 0
        for dungeon in path:
            minimum_require_fatigue, exhaust_fatigue = dungeon 
            if current_fatigue < minimum_require_fatigue:
                break
            current_fatigue -= exhaust_fatigue
            dungeon_clear_counter += 1
        max(max_counter, dungeon_clear_counter)
    return max_counter