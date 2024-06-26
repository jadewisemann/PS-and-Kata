/*
```yaml
problem: "Sum of Digits / Digital Root"
tags: MATHEMATICS, ALGORITHMS
difficulty: 6-kyu
source: codewars
link: https://www.codewars.com/kata/541c8630095125aba6000c00
```
*/

const digitalRoot = n => n < 10 ? n : digitalRoot( digitalRoot(Math.floor(n / 10)) + n % 10);