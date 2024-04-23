"""
problem: '잃어버린 괄호'
tags: 수학, 그리디, 문자열, 파싱
difficulty: 실버 2
source: baekjoon
link: https://www.acmicpc.net/problem/1541
"""

"""
1.   a - b


2.   a - b + c
2.1. a - b + c
2.1. a - (b + c) 
    = a - b - c

뒤에가 양수 일때 묶으면 최종결과가 음수가 됨

3.   a - b - c
3.1. a - b - c
3.2. a - (b - c) 
    = a - b + c

뒤에가 음수 일때 묶으면 뒷수가 양수가 됨

4. a - b - c + d
4.1. - b가 뒤를 묶으면,
    a -(b - c) + d
    a - b + c + d
4.1.a 
    a - (b - c + d)
    a - b + c - d
4.2 -c
    a - b - (c+d)
    a - b - c - d

5. a -b + c + d + e - f
a - (b + c + d + e) - f 
a - b - c - d - e - f

-괄화안의 값이 얼마나 커지느냐 = 플러스를 얼마나 참여 시키느냐
-를 만난 순가 닫아 버리고, 그 -가 다시 열면 된다.
즉
()  - () - () - () - () - () - () - () - ()
""" 


first,*rest = [sum(map(int, numbers.split("+"))) for numbers in input().split("-")]
print(first,sum(rest))