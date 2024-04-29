/*
```yaml
problem: "The Millionth Fibonacci Kata"
tags: mathematics, algorithms
difficulty: 3-kyu
source: codewars
link: [codewars](https://www.codewars.com/kata/53d40c1e2f13e331fc000c26)
```
*/

const fib = n => {

  const matrixMultiply = (a, b) => {
    return [
      [(a[0][0] * b[0][0] + a[0][1] * b[1][0]), (a[0][0] * b[0][1] + a[0][1] * b[1][1])],
      [(a[1][0] * b[0][0] + a[1][1] * b[1][0]), (a[1][0] * b[0][1] + a[1][1] * b[1][1])]
    ];
  }

  const matrixPower = (matrix, n) => 
    n === 1 ? matrix :
    n % 2 === 0 ? (() => {
      const halfPower = matrixPower(matrix, n / 2)
      return matrixMultiply(halfPower, halfPower)
    }) () : matrixMultiply(matrix, matrixPower(matrix, n - 1))

  if (n === 0) return BigInt(0);

  let isNegative = false;
  if (n < 0) {
    isNegative = true;
    n = -n
  }

  const resultMatrix = matrixPower([
    [BigInt(1), BigInt(1)],
    [BigInt(1), BigInt(0)]
  ], n);

  let result = resultMatrix[1][0];

  if (isNegative && n % 2 === 0) result = -result;

  return result;
}