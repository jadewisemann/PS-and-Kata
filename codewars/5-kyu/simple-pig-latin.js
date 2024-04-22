/*
```yaml
problem: "Simple Pig Latin"
tags: REGULAR EXPRESSIONS, ALGORITHMS
difficulty: 5-kyu
source: codewars
link: https://www.codewars.com/kata/520b9d2ad5c005041100000f/
```
*/

const pigIt = (str) => 
  str
    .split(" ")
    .map(word =>
      /[a-z]/gi.test(word)
        ? [word.slice(1), word[0], "ay"].join("")
        : word
    ).join(" ")

g