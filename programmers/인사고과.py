"""

```yaml
problem: "인사고과"
tags: 
difficulty: LV3
source: programmers
link: https://school.programmers.co.kr/learn/courses/30/lessons/152995
```

###### 문제 설명

완호네 회사는 연말마다 1년 간의 인사고과에 따라 인센티브를 지급합니다.
각 사원마다 근무 태도 점수와 동료 평가 점수가 기록되어 있는데 만약 어떤 사원이 다른 임의의 사원보다 두 점수가 모두 낮은 경우가 한 번이라도 있다면 그 사원은 인센티브를 받지 못합니다.
그렇지 않은 사원들에 대해서는 두 점수의 합이 높은 순으로 석차를 내어 석차에 따라 인센티브가 차등 지급됩니다.
이때, 두 점수의 합이 동일한 사원들은 동석차이며, 동석차의 수만큼 다음 석차는 건너 뜁니다.
예를 들어 점수의 합이 가장 큰 사원이 2명이라면 1등이 2명이고 2등 없이 다음 석차는 3등부터입니다.

각 사원의 근무 태도 점수와 동료 평가 점수 목록 `scores`이 주어졌을 때, 완호의 석차를 return 하도록 solution 함수를 완성해주세요.

---

##### 제한 사항

-   1 ≤ `scores`의 길이 ≤ 100,000
-   `scores`의 각 행은 한 사원의 근무 태도 점수와 동료 평가 점수를 나타내며 [a, b] 형태입니다.
    -   `scores`[0]은 완호의 점수입니다.
    -   0 ≤ a, b ≤ 100,000
-   완호가 인센티브를 받지 못하는 경우 -1을 return 합니다.

---

##### 입출력 예

| scores | result |
| --- | --- |
| [[2,2],[1,4],[3,2],[3,2],[2,1]] | 4 |

---

##### 입출력 예 설명

5 번째 사원은 3 번째 또는 4 번째 사원보다 근무 태도 점수와 동료 평가 점수가 모두 낮기 때문에 인센티브를 받을 수 없습니다.
2 번째 사원, 3 번째 사원, 4 번째 사원은 두 점수의 합이 5 점으로 최고점이므로 1 등입니다.
1 등이 세 명이므로 2 등과 3 등은 없고 1 번째 사원인 완호는 두 점수의 합이 4 점으로 4 등입니다.

"""

def solution(scores):
        
    answer = 0

    target_attitude, target_peer_review = scores[0]
    target_score_sum = target_attitude + target_peer_review

    scores = sorted(scores[1:],key=lambda x: (-x[0],x[1]))

    prev_max_peer_review = 0
    for attitude, peer_review in scores:
        
        if (target_attitude < attitude
        and target_peer_review < peer_review):
            return -1
        
        if peer_review < prev_max_peer_review: 
            continue
            
        prev_max_peer_review = peer_review
        if attitude + peer_review > target_score_sum:
            answer += 1
            
        return answer + 1
