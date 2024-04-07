def sieve_of_eratosthenes(target_number):
    # n만큼의 배열을 생성
    isPrimes = [True] * (target_number+1)
    # 0, 1은 False, 소수가 아님
    isPrimes[0], isPrimes[1] = [False] * 2
    primes = []
    
    square_root = int(target_number**(0.5))
    
    # 2에서 n의 제곱근까지 모든 수를 순회
    for number in range(2, square_root + 1):
        # 그 수가 소수라고 표시가 되어 있다면, 
        if isPrimes[number]:
            # 그 수의 제곱 부터 n까지의 숫자 중, 수의 배수를 제외
            for i in range(number*number, target_number+1, number):
                isPrimes[i] = False
    
    # 배열의 모든 수를 순회 하면서 소수면 추가.
    for number, isPrime in enumerate(primes):
        if isPrime:
            primes.append(number)

    return primes
