
### [kata][.js][5-kyu] RGB to Hex Conversion ( TIL 24 04 25 )


```yaml
problem: "Simple Pig Latin"
tags: REGULAR EXPRESSIONS, ALGORITHMS
difficulty: 5-kyu
source: codewars
link: https://www.codewars.com/kata/520b9d2ad5c005041100000f/
```

# problem

RGB(0-255, 0-255, 0-255)를 HEX(FFFFFF) 로 전환하는 함수를 만들어라.

# 🤔

## RGB & HEX

RGB는 빛의 삼원색의 각 색상을 0에서 255으로 나타낸 것이다.
r, g, b를 각각 받아서, HEX 코드로 변환하면 된다.

HEX는 hexadeca, 16을 의미하는데, 255는 16진법을 2자리써서 나타낼 수 있는 가장 큰 수이다. ($$16**2 = 255$$)

> 16진법의 수
> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f

결국 정리해보자면,
숫자를 받아서, 16진법으로 변환하고 양식에 맞게 출력하면 된다.

## 16진법

16진법은 모듈러 연산으로 나머지를 가져서 몫고, 나머지에 대해서 대응시켜도 된다.

```js
hexArr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
const numToHex = number => [hexArr[Math.floor(number/16)],hexArr[number%16]].join('')
```
근데 훨씬 간단한 방법인 `.toString()`이 있다. 

### `.toString()`

`.toString()` 은 메소드인데 인자로 뭘 받을까? 기본값으로 `10`이 들어가 있어서 10 진법 숫자로 변환이 되는 것이지
몇 진법으로 변환할지를 인자로 넣어 줄 수 있다.

따라서, `toString(16)`으로 해주면 된다.

## 대문자처리

16진법에서는 상관없지만, 컴퓨터에서는 전통적으로 11-15에 해당하는 a-f는 대문자를 사용한다.
Hex 또한 그렇기에 대문자 처리를 하자

`String.toUppercase()`를 사용한다.
`String`에 사용가능한 메소드인데, 위에서 `toString()`으로 형변환을 하기때문에 걱정하지 않아도 된다.

## 자리 채우기

16미만의 수는 16진법으로는 모두 한자리의 수가 된다.
HEX 코드는 늘 6자리이기 때문에 2자리를 만들어야 한다.
이를 위해 `String.padStart()`를 사용하자.
- `pad`는 `padding`이라는 뜻인데 채우는 것을 의미한다.
- - 인자를 두개를 받는다
  - 앞 인자: 몇개의 문자까지 채울지
  - 뒤 인자: 빈 공간을 무엇을 채울지
- `padStart`와 `padEnd`가 있는데, 앞에서 채울지, 뒤에서 채울지가 다르다
  - `padStart(5, '*')`: `"123"` $$\Rightarrow$$ `**123`
  - `padEnd(5, '*')`: `"123"` $$\Rightarrow$$ `123**`

우리는 `2`자를 `앞`에서 `0`으로 채우기 때문에 
`padStart(2, '0')`을 사용한다.

## 예외 처리

하고, `join`으로 합쳐서 던졌는데... 예외가 난다.

RGB가 `-20` 이나 `300` 이 들어온다...
`-20`은 `0`으로, `300`은 `255`로 취급해서, 에러가 발생안하고, 6자리를 안넘어가게 해야 한다.

### 3항 연산자

개인적으로 좋아한다... 다른 사람들은 싫어하자만.
3항 연산자를 중첩으로 쓰자. 가독성에는 신경을 써서 배치를 해야한다.

```js
 .map((color) => (
    color < 0 ? 0 :
    color > 255 ? 255
    : color)
```

0 미만은 0 , 255 초과는 255로 처리해준다.

### Math.max, Math.min

내장함수인  `Math.max` 와 `Math.min`을 쓸 수 도 있다.

```js
  .map((color) => Math.max(Math.min(255, color), 0)
```
# solution w/code

## #1 first answer

```js
const rgb = (r, g, b) => [r, g, b]
 .map((color) => (
    color < 0 ? 0 :
    color > 255 ? 255
    : color)
    .toString(16)
    .padStart(2, "0")
    .toUpperCase()
  ).join("")
```

## #2 use max, min

**간결**

```js
const rgb = (r, g, b) => [r, g, b]
   .map((color) => Math.max(Math.min(255, color), 0)
    .toString(16)
    .padStart(2, "0")
    .toUpperCase()
  ).join("")
```

## #3 use spread syntax 

이게 더 안전한 방식이다.
인자의 개수가 관계 없이 받아서 처리하기 때문.

```js
const rgb = (...args) => args
  .map((color) => Math.max(Math.min(255, color), 0)
    .toString(16)
    .padStart(2, "0")
    .toUpperCase()
  ).join("")
```

# review : 🙂

## 🔥🔥 & ⌛:  20 min

이런 문제들은 코드가 짧고 이해하기 쉬워 글을 작성하는 노력이 아까워지곤 하는것 같다. 