from itertools import product

def solution(numbers, target):
    return list(map(sum, product(*[(-number, +number) for number in numbers]))).count(target)
