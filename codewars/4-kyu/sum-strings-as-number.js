/*
```yaml
problem: "Sum Strings as Number"
tags: string, big-integers, algorithms
difficulty: 4-kyu
source: codewars
link: https://www.codewars.com/kata/5324945e2ece5e1f32000370
```
*/

const sumStrings = (a, b) =>  (BigInt(a) + BigInt(b)).toString()

console.log(sumStrings('123', '456'))

console.log(toString(123))