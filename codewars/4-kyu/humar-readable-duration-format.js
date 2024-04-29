/*
```yaml
problem: "Human readable duration format"
tags: string, data-time, algorithm
difficulty: 4-kyu
source: codewars
link: https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/javascript
```
*/

const TIME_UNITS = {
  second: 1,
  minute: 60,
  hour: 60,
  day: 24,
  year: 365
}

const formatDuration = seconds => {
  const modular = (num, divisor) => [Math.floor(num / divisor), num % divisor];

  const result = Object.entries(TIME_UNITS)
    .reduce(([arr, acc], [key, val]) => {
      acc *= val;
      arr.push([key, acc]);
      return [arr, acc]
    }, [[], 1])[0]
    .reverse()
    .reduce(([arr, acc], [key, val]) => {
      if (seconds >= val) {
        acc = Math.floor(seconds / val);
        arr.push([key, acc])
        seconds %= val
      } return [arr, acc]
    }, [[], 1])[0]
    .filter(([_, val]) => val > 0)
    .map(([key, val]) => `${val} ${key}${val > 1 ? 's' : ''}`);
  
  return result.length > 1
    ? `${result.slice(0, -1).join(", ")} and ${result[result.length - 1]}`
    : result[0] || "now";
};  