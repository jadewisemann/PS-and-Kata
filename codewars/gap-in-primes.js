function gap(g, m, n) {

  var lastPrime = 0;
  
  const isPrime = num => { 
    for (var i = 2; ( i ** 2 ) <= num; i++) {
      if (num % i == 0) return false;
    } return true;
  }
  
  for (var number = m; number <= n; number++)
    if (isPrime(number)) { 
      if (number - lastPrime == g) return [lastPrime, number];
      else lastPrime = number;
    }
  
  return null;
}