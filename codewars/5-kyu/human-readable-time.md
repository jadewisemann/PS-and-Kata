```
problem: 'Human Readable Time'
tags: DATE TIME, MATHEMATICS, ALGORITHMS
difficulty: 5-kyu
source: codewars
link: https://www.codewars.com/kata/52685f7382004e774f0001f7/
```

# problem : 'Human Readable Time'

초를 사람이 읽을 수 있는 숫자 포멧을 바꾸는 것인데 생각보다 귀찮은 부분들이 있다.

# 🤔

## simple is best

문제 자체는 심플하다. 로직을 바로 구현한 코드이다.

```js
const formatTime = seconds => {
  let hours = Math.floor(seconds / 3600)
    .toString()
    .padStart(2, "0");
  let minutes = Math.floor((seconds % 3600) / 60)
    .toString()
    .padStart(2, "0");
  let remainingSeconds = (seconds % 60).toString().padStart(2, "0");

  return `${hours}:${minutes}:${remainingSeconds}`;
};
const padZero = x => x.toString().padStart(2, "0");

const humanReadable = seconds =>
  [
    Math.floor(seconds / (60 * 60)),
    Math.floor((seconds / 60) % 60),
    seconds % 60,
  ]
    .map(padZero)
    .join(":");
```

흠,,,

너무 반복이 많다.

## outer function

외부의 코드를 선언해서, 반복되는 코드를 줄였다. 하나로 묵어 주었다.

```js
const padZero = x => x.toString().padStart(2, "0");

const humanReadable = seconds =>
  padZero(Math.floor(seconds / (60 * 60))) +
  ":" +
  padZero(Math.floor((seconds / 60) % 60)) +
  ":" +
  padZero(seconds % 60);
```

하지만 문제는 모든 대상에게 적용된다는 것이지, 로직이 길다는 것이 아니다.

## array literal w.maps

에로우 펑션과 배열 리터럴로 배열을 만들면, map을 사용할 수 있다.

```js
const padZero = x => x.toString().padStart(2, "0");

const humanReadable = seconds =>
  [
    Math.floor(seconds / (60 * 60)),
    Math.floor((seconds / 60) % 60),
    seconds % 60,
  ]
    .map(padZero)
    .join(":");
```

_어라?_ 이러면 이제 `padZero`는 단 한번만 쓰이는 함수가 되어 버린다.
치워주자.

```js
const humanReadable = seconds =>
  [
    Math.floor(seconds / (60 * 60)),
    Math.floor((seconds / 60) % 60),
    seconds % 60,
  ]
    .map(x => x.toString().padStart(2, "0"))
    .join(":");
```

$\huge\text{Ta\,-\,Da!}$

# review : 🤨

## 🔥🔥🔥

생각할 부분이 꽤 있었던 것 같다.
반복을 줄이는 것이 모든 프로그래머의 목표이니, 다른 사람들의 풀이에서도 코드의 반복과 길이를 줄이려는 다양한 방법들이 보였는데,
변수의 이름을 줄이거나 하드 코딩의 패턴이 많아서, 이를 피해가기 위해 노력하였고,
`map`과 배열 리터럴을 사용해 만족스러운 결과를 보였다고 생각한다.

#

######
