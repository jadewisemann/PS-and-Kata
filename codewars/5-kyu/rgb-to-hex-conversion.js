/*
```yaml
problem: 'RGB To Hex Conversion'
tags: ALGORITHMS
difficulty: 5-kyu
source: codewars
link: https://www.codewars.com/kata/513e08acc600c94f01000001
```
*/
// const rgb = (r, g, b) => [r, g, b]
//  .map((color) => (
//     color < 0 ? 0 :
//     color > 255 ? 255
//     : color)
//     .toString(16)
//     .padStart(2, "0")
//     .toUpperCase()
//   ).join("")


// const rgb = (r, g, b) => [r, g, b]
//    .map((color) => Math.max(Math.min(255, color), 0)
//     .toString(16)
//     .padStart(2, "0")
//     .toUpperCase()
//   ).join("")

const rgb = (...args) => args
  .map((color) => Math.max(Math.min(255, color), 0)
    .toString(16)
    .padStart(2, "0")
    .toUpperCase()
  ).join("")
