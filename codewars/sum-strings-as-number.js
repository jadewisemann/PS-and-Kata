/*

```yaml
problem: "Sum Strings as Number"
tags: string, big-integers, algorithms
difficulty: 4-kyu
source: codewars
link: https://www.codewars.com/kata/5324945e2ece5e1f32000370
```

Given the string representations of two integers,
return the string representation of the sum of those integers.

For example:

```javascript
sumStrings('1','2') // => '3'
```

A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

*/

const sumStrings = (a, b) =>  (BigInt(a) + BigInt(b)).toString()

console.log(sumStrings('123', '456'))

console.log(toString(123))