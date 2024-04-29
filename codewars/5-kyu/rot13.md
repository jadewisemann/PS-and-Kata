

### [kata][5-kyu][.js] Rot13 ( TIL 24 04 28 )

```yaml
problem: 'Rot13'
tags: CIPHERS, FUNDAMENTALS
difficulty: 5-kyu
source: codewars
link: https://www.codewars.com/kata/530e15517bc88ac656000716
```

# problem

13개씩 움직이는 시저 암호를 출력하는 함수를 만들어라.

# 🤔

인덱스만큼 움직이는 알파벳? 말 안해도 ascii 코드를 써야 할 것이다.
js는 `char()`는 없어도, `String.fromCharCode()`와 `String.prototype.charCodaAt()`이 있다.
뭘 해야할지는 명확하다. 때문에 생길 수 있는 오류를 잘 피해가야 한다.
여기서 가장 핵심은 두가지이다.
1. 대소문자 처리
2. 범위 처리

## 대소문자 처리

ascii에서 영어 대문자와 소문자는 연속되지 않는다.
`A-Z: 65-90` , `a-z:97-122`
때문에 대문자와 소문자의 범위가 다르다른 점을 염두에 두어야 한다.

## 범위 처리

알파벳은 26개 밖에 없고, `m` 이후에는 ascii 코드를 13을 더하면 이상한 값이 나올수 밖에 없다.
이를 주의해야 한다.

# solution w/code

우선 이것을 명확하게 하자.

> 하드코딩을 하지 않을 것이다.

이 문제는 하드코딩을 하면 참 좋은 문제다.
알파벳을 전부 만들어 놓고, `String.prototype.substring()`을 이용하면 안전하게 13을 기준으로 앞뒤를 나눠, 
인덱스를 기준을 간편하게 비교가 가능하다.
일반적인 암호체계에서는 이런방식이 불가능하지만, 이 문제는 변환대상이 54개가 단방향으로 가기 때문에 딱 적당하다.
그럼에도, 하드코딩을 하지는 않을 것이다.

## 1st

첫 번쨰 코드다.
`replace`를 이용, 정규표현식으로 대소문자 가리지 않고 알파벳을 고른후,
콜백 함수를 이용해서 ascii 코드를 구하고 13을 더해서 다시 char로 바꿔준다.

- 범위를 초과하는 것을 막기위해서, `char`와  `Z`와의 비교를 통해서 대소문자인지 판별해, 가능한 ascii 코드의 상한을 구한다.
- 그 후, ascii 코드에 13을 직접 더해, 상한을 초과하는지 확인한다.
- 초과하면 26을 빼줘서, 범위를 초과하지 않고, 한바퀴 돌아오도록 만든다.

```js
const rot13 = message => message.replace(
  /[a-z]/gi, char => String.fromCharCode(
    (char <= 'Z' ? 90 : 122) >= (char = char.charCodeAt(0) + 13)
      ? char
      : char - 26)
  );
```


## refactoring 

그런데,,, 생각을 좀 바꿔보면,

```js
char.charCodeAt(0) + 13
? char
: char - 26
```

을

```js
char.charCodeAt(0) + 13
? char.charCodaAt(0) + 13
: char.charCodaAt(0) + 13 - 26
```

로 볼 수 있다.

결국 특정 값을 기준으로 +13, -13을 해주는 것인데, 그러면 대소문자 비교도 필요 없어 진다.
(알파벳이 26자이기 때문에 1에 13은 +13, 그 이후는 -13을 해주면 범위를 나가지 않는다.)

## 2nd

대소문자 비교를 제외하고 지금 처리중인 `char`가 13이전인지 이후인지만 보고 처리하면 된다.

```js
const rot13 = message => message.replace(/[a-z]/gi,
  char => String.fromCharCode(
    char.charCodeAt(0) + (char.toLowerCase() <= 'm'? +1 : -1) * 13
  )
)
```

`m`이 정확히 13번째 문자이기 때문에 `m` 이하면 -13을 해주고 초과면 +13을 해주면 된다.



# review :  🙂 


## 🔥🔥🔥

생각보다는 어려웠다.
로직이 어렵다기 보다는 범위 처리를 어떻게 이쁘게 할까를 고민했다.
함수들이 좀 길어서 어쩔수는 없지만, 가능한 간결하고 가독성 있게 만들 수 있었다.
