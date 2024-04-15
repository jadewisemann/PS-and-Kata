def solution(s):
    answer = 0
    while s:
        X = s[0]
        is_X = 0
        not_X = 0
        
        for idx,  letter in enumerate(s):

            if letter == X:
                is_X += 1
            else:
                not_X += 1
            
            if is_X == not_X:
                answer += 1
                s = s[idx+1:]
                break
        
        else:
            if is_X != not_X:
                answer += 1
            break
        
    return answer