/*
```yaml
problem: 'Rot13'
tags: CIPHERS, FUNDAMENTALS
difficulty: 5-kyu
source: codewars
link: https://www.codewars.com/kata/530e15517bc88ac656000716
```
*/

const rot13 = message => message.replace(
  /[a-z]/gi, char => String.fromCharCode(
    (char <= 'Z' ? 90 : 122) >= (char = char.charCodeAt(0) + 13)
      ? char
      : char - 26)
  );

