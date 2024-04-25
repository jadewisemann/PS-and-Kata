"""
```yaml
problem: '잃어버린 괄호'
tags: 수학, 그리디, 문자열, 파싱
difficulty: silver2
source: baekjoon
link: https://www.acmicpc.net/problem/1541
```
"""

first,*rest = [sum(map(int, numbers.split("+"))) for numbers in input().split("-")]
print(first - sum(rest))