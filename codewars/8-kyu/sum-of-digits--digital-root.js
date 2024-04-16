/*
```yaml
problem: "Sum of Digits / Digital Root"
tags: MATHEMATICS, ALGORITHMS
difficulty: 6-kyu
source: codewars
link: https://www.codewars.com/kata/541c8630095125aba6000c00
```
*/
const digitalRoot = n => {
  let result = 0
  while (n > 0) {
    result += n % 10
    n = Math.floor(n/10)
  }
  return result >= 10 ? digitalRoot(result) : result 
}
