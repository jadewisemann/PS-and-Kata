
def linear_sieve(number):
    
    smallest_prime_factor = [0, 1] + [0] * (number)
    primes = []
    
    for i in range(1, (number) + 1):
        
        if not smallest_prime_factor[i]:
            primes.append(i)
            smallest_prime_factor[i] = i

        for prime in primes:
            if i * prime > number: break
            smallest_prime_factor[i*prime] = prime  
            if i % prime == 0: break
            
