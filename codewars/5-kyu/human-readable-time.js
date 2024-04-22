```
problem: 'Human Readable Time'
tags: DATE TIME, MATHEMATICS, ALGORITHMS
difficulty: 5-kyu
source: codewars
link: https://www.codewars.com/kata/52685f7382004e774f0001f7/
```

const humanReadable = seconds =>
  [
    Math.floor(seconds / (60 * 60)),
    Math.floor((seconds / 60) % 60),
    seconds % 60,
  ]
    .map(x => x.toString().padStart(2, "0"))
    .join(":");