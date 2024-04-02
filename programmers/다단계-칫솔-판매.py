def solution(enroll, referral, sellers, amount):
    
    # 딕셔너리 생성
    profits = {name: 0 for name in enroll}
    referral_dict = {enroll[i]: referral[i] for i in range(len(enroll))}
    
    # 순회
    for idx in range(len(sellers)):
        seller = sellers[idx]
        profit = amount[idx] * 100
        
        # 추천관계 확인
        recommendee = seller 
        while recommendee != "-" and profit > 0:
            commission = profit // 10
            profits[recommendee] += profit - commission
            recommendee = referral_dict[recommendee]
            profit = commission
    
    return [profits[name] for name in enroll]