def solution(s):
    answer = 0
    criteria = ""
    criteria_counter = 0
    dict_counter = {}
    
    for  idx, letter in enumerate(s):
        # 1> 기준 없음 => letter 가 기준
        if not criteria:  
            criteria = letter
            criteria_counter += 1
        # 2> 기준 있음

        # 2> a> 기준 개수 측정
        elif letter == criteria:
            criteria_counter += 1
        
        # 2> b> 기준 왜 문자의 개수 측정 
        else:
            # 해당 문자가 있는지 확인
            # 없다면, 카운터를 1로 선언
            if letter in dict_counter.keys():
                dict_counter[letter] += 1
            # 있다면, 1추가
            else:    
                dict_counter[letter] = 1
            # 기준이랑 개수 비교
            if dict_counter[letter] == criteria_counter:
                # 정답 추가
                answer += 1
                # 초기화
                criteria = ""
                criteria_counter = 0
                dict_counter = {}

    return answer