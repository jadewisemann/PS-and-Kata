/*

```yaml
problem: "The Millionth Fibonacci Kata"
tags: mathematics, algorithms
difficulty: 3-kyu
source: codewars
link: [codewars](https://www.codewars.com/kata/53d40c1e2f13e331fc000c26)
```


The year is 1214.
One night, Pope Innocent III awakens to find the the archangel Gabriel floating before him.

Gabriel thunders to the pope:

> Gather all of the learned men in Pisa, especially Leonardo Fibonacci.
In order for the crusades in the holy lands to be successful,
these men must calculate the *millionth* number in Fibonacci's recurrence.
Fail to do this, and your armies will never reclaim the holy land. It is His will.

The angel then vanishes in an explosion of white light.

Pope Innocent III sits in his bed in awe.
*How much is a million?* he thinks to himself.
He never was very good at math.
He tries writing the number down,
but because everyone in Europe is still using Roman numerals at this moment in history,
he cannot represent this number.
If he only knew about the invention of zero, it might make this sort of thing easier.

He decides to go back to bed.
He consoles himself, *The Lord would never challenge me thus;
this must have been some deceit by the devil. A pretty horrendous nightmare, to be sure.*

Pope Innocent III's armies would go on to conquer Constantinople (now Istanbul),
but they would never reclaim the holy land as he desired.

---

In this kata you will have to calculate `fib(n)` where:

```
fib(0) := 0
fib(1) := 1
fib(n + 2) := fib(n + 1) + fib(n)
```

Write an algorithm that can handle `n` up to `2000000`.

Your algorithm must output the exact integer answer, to full precision.
Also, it must correctly handle negative numbers as input.

**HINT I**:
Can you rearrange the equation `fib(n + 2) = fib(n + 1) + fib(n)` to find `fib(n)`
if you already know `fib(n + 1)` and `fib(n + 2)`?
Use this to reason what value `fib` has to have for negative values.
---

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