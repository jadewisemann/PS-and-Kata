function isPrime(num) {
    for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++) {
        if (num % i === 0) return false;
    }
    return num > 1;
}

function gap(g, m, n) {
    let lastPrime = 0;
    for (let i = m; i <= n; i++) {
        if (isPrime(i)) {
            if (i - lastPrime === g) return [lastPrime, i];
            lastPrime = i;
        }
    }
    return null; // 조건에 맞는 소수 쌍이 없을 경우
}

// 예시 사용법
console.log(gap(2, 5, 7)); // [5, 7]
console.log(gap(2, 5, 5)); // null
console.log(gap(4, 130, 200)); // [163, 167]
console.log(gap(6, 100, 110)); // null
