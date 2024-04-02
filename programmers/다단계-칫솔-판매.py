
def solution(enroll, referral, sellers, amount):
    # 딕셔너리 생성
    profits = {name: 0 for name in enroll}
    referral_dict = {enroll[i]: referral[i] for i in range(len(enroll))}
    
    # 순회
    for idx in range(len(sellers)):
        seller = sellers[idx]
        profit = amount[idx] * 100
        recommendee = seller  # 알고 리즘상 필요 없는 부분 이지만, 관게의 의미를 명확하기 해주고자 사용
        # 추천관계 확인
        while recommendee != "-" and profit > 0:
            commission = profit // 10
            profits[recommendee] += profit - commission
            recommendee = referral_dict[recommendee]
            profit = commission
    
    return [profits[name] for name in enroll]

# 예제 입력
enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
sellers = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

# 함수 실행
print(solution(enroll, referral, sellers, amount))
