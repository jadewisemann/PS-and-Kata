function findPrimes(targetNumber) {
  // 소수인지 확인하는 배열, 인덱스는 숫자고, 0, 1은 아님
  const isPrimes =  [ false, false, ...Array(targetNumber - 1).fill(true)];
  const primes = [];
  const squareRoot = Math.sqrt(targetNumber) 

  // 2에서 타겟 숫자의 제곱근까지의 모든 숫자를 전부 순회
  for (let number = 2; number <= squareRoot; number++) {
    // 해당 숫자가 소수면, 그 숫자의 배수들을 모두 소수가 아니라고 표시
    if (isPrimes[number]) {
      for (let multiple = number * number; multiple <= targetNumber; multiple += number) {
        isPrimes[multiple] = false;
      }
    }
  }
  // 소수인지 확인하는 배열을 전부 둘면서 true면 소수에 담는다. 
  for (const [index, isPrime] of isPrimes.entries()) {
    if (isPrime) {
      primes.push(index);
    }
  }
  return primes;
}
