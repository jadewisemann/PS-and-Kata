/*

```yaml
problem: "Multiples of 3 or 5"
tags: MATHEMATICS, ALGORITHMS
difficulty: 6-kyu
source: codewars
link: https://www.codewars.com/kata/514b92a657cdc65150000006/
```
*/
const solution = number => (number < 1 ) ? 0 : 
  [...new Array(number).keys()]
    .filter(n => n % 3 == 0 || n % 5 == 0)
    .reduce((acc, cur) => acc + cur)
