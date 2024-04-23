/*
```
problem: 'Snail'
tags: ARRAYS, ALGORITHMS
difficulty: 4-kyu
source: codewars
link: https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
```
*/





const snail = array => {
  var result = [];
  while (array.length) {
    result = [...result, ...array.shift()]
    array.forEach(row => result.push(row.pop()))
    array.reverse().forEach(row => row.reverse());
  }
  return result;
}