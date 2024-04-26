

### [kata][5-kyu][.js] Calculating with Functions ( TIL 24 04 26 )


```yaml
problem: 'Calculating with Functions'
tags: FUNCTIONAL-PROGRAMMING
difficulty: 5-kyu
source: codewars
link: https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
```

# problem

```js
seven(times(five())); // must return 35
four(plus(nine())); // must return 13
eight(minus(three())); // must return 5
six(dividedBy(two())); // must return 3
```

위와 같이 작동하는 0-9까지의 숫자함수와 사칙연산을 만들어라. 

# 🤔

이거 문제 좋은것 같다.
다른 카타를 풀면서 아름답다고 느낀 그런것 아니지만, 고차 함수를 불러서 사용한다는 것이 무엇인지 잘 알 수 있었다.


## 숫자 함수

숫자 함수는 심플하다.

숫자함수 사칙연산 함수에게 불렸을 때는 숫자로, 취급되고, 
사칙연산을 인자로 가졌을때는 그 함수를 실행한다.

따라서 삼항 연산자로 인자가 있는지 유무를 확인하고 인자가 없으면 숫자,
있으면 인자로 들어온 함수의 인자로 들어간 값을 반환하도록 짜준다.

```js
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
```

## 사칙연산

사칙연산은 좀 복잡할 수 있는데 생각해보면 간단한다.

```js
const plus      = right => left => left + right 
const minus     = right => left => left - right
const times     = right => left => left * right
const dividedBy = right => left => Math.floor(left / right)
```

`right`를 받아서 `left`를 받는 함수를 리턴하는 것이다.

괄호를 쳐서 보면 다음과 같다.

```js
const plus = right => {
  return (left) => {
    return left+ right
  }
}
```

즉 함수를 받아서, 리턴하는 함수의 형태가 되는 것이다.

다만 의문이 생길 수 있는 부분이 호출방식일 것이다.

저런형태라고 한다면 호출방식은 응당

```js
plus(5)(3)  // 5 + 3 = 8
```

이어야 한다. 하지만 문제의 호출방식은

```js
five(plus(three()))
```

인것이다. 이를 위해서 숫자가 자기 자신에게 인자로 들어온 함수에게 던저지게 설계를 하였다.

- `three()`는 인자가 없으니 `3`과 같다.
- `five(plus(3))`는 함수에 자기 자신을 던진 값을 반환하므로 `plus(3)(5)`가 된다.


# review : 🙂

## 🔥🔥🔥 & ⌛:  30 min

이 문제 정말 좋았다.
누가 고차 함수가 뭐냐고 물어보면 이 문제를 풀어보라고 할 것 같다.

# code

```javascript
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
```