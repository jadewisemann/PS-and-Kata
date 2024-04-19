/*
```yaml
problem: "Stop gninnipS My sdroW!"
tags: STRINGS, ALGORITHMS
difficulty: 6-kyu
source: codewars
link: https://www.codewars.com/kata/5264d2b162488dc400000001/
```
*/

const spinWords = (sentence) => {
  return sentence
    .split(' ')
    .map(word => word.length >= 5 ? word.split('').reverse().join('') : word)
    .join(' ');
}