/*
```yaml
problem: 'Calculating with Functions'
tags: FUNCTIONAL-PROGRAMMING
difficulty: 5-kyu
source: codewars
link: https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
```
*/

const zero  = fn => fn ? fn(0) : 0;
const one   = fn => fn ? fn(1) : 1;
const two   = fn => fn ? fn(2) : 2;
const three = fn => fn ? fn(3) : 3;
const four  = fn => fn ? fn(4) : 4;
const five  = fn => fn ? fn(5) : 5;
const six   = fn => fn ? fn(6) : 6;
const seven = fn => fn ? fn(7) : 7;
const eight = fn => fn ? fn(8) : 8;
const nine  = fn => fn ? fn(9) : 9;

const plus      = right => left => left + right 
const minus     = right => left => left - right
const times     = right => left => left * right
const dividedBy = right => left => Math.floor(left / right)

