/*

```yaml
problem: "Human readable duration format"
tags: string, data-time, algorithm
difficulty: 4-kyu
source: codewars
link: https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/javascript
```
## Problem 

Your task in order to complete this Kata is to write a function
which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer.

If it is zero, it just returns "now".
Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

## example

```
* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
```

## detail rules

The resulting expression is made of components like 4 seconds, 1 year, etc.
In general, a positive integer and one of the valid units of time, separated by a space.
The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", ").
Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one.
Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times.
So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero.
Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible".
It means that the function should not return 61 seconds, but 1 minute and 1 second instead.
Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
*/

// 년, 일 , 시간 , 분 초 로 읽을수 있게 됨

//

const formatDuration = seconds => {
  const modular = (num, divisor) => [Math.floor(num / divisor), num % divisor];

  const [tmp_minute, second] = modular(seconds, 60);
  const [tmp_hour, minute] = modular(tmp_minute, 60);
  const [tmp_day, hour] = modular(tmp_hour, 24);
  const [year, day] = modular(tmp_day, 365);

  const units = [[year, "year"], [day, "day"], [hour, "hour"], [minute, "minute"], [second, "second"]];

  const result = units
    .filter(([value, _]) => value > 0)
    .map(([value, label]) => `${value} ${label}${value > 1 ? 's' : ''}`);
  
  return result.length > 1 ?`${result.slice(0, -1).join(", ")} and ${result[result.length - 1]}`: result[0] || "now";
};