

### [PS][5-kyu][.js] title ( TIL 24 04 29 )

```yaml
problem: 'The Hashtag Generator'
tags: STRINGS, ALGORITHMS
difficulty: 5-kyu
source: codewars
link: https://www.codewars.com/kata/52449b062fb80683ec000024
```

# problem

일반 문자열을 헤쉬테그로 바꾼다.
- 헤쉬태그는 맨앞에 `#` 이 붙는다.
- 문자들은 카멜케이스
- 140자가 넘거나 문자열이 비어 있으면, `false` 반환

# 🤔

뭐,,, split하고 순회하면서 앞만 toUpperCase 치고 join하고 조건 검사하면 될 것같다.

## solution #1

```js
const generateHashtag = (str) => {

  const trimmedStr = str.trim();
  if (!trimmedStr) return false;

  const hashtag = '#' + trimmedStr
    .split(' ')
    .filter(Boolean)
    .map(word => word.replace(/^\w/, (c) => c.toUpperCase()))
    .join('');

  return hashtag.length > 140 ? false : hashtag;
};
```

### 비어있는 문자열 확인 

- 우선 `trim`을 통해 문자열 양옆을 치운다.
- 그리고 만약 다듬어진 문자열이 비어 있으면 바로 false를 return한다.

### 해쉬태그 생성

- 그 후 문자열을 공백을 기준으로 나눈다.
-  `filter(Boolean)` 을 걸어서, 의미가 없는, `falsy`한 값들을 걸러낼 수 있다.
  - 빈 문자열, 이스케이프 시퀀스 등,
- 그리고 첫 문자를 regExp의 첫 문자를 잡아오는 `^\w`를 이용해서, 대문자로 바꿔서 카멜케이스를 충족한다.
- 그리고 합친다.

### 길이 예외 처리

- 리턴 직전에 해쉬태그 길이를 확인한다.
- 원본 문자열은 여백도 있기 때문에 길이를 확인하기 적절하지 못하다.


## solution #2

3가지를 적용해서, 문자열을 로직을 간결하게 만들자.

1. `filter(Boolean)`은 없어도 별 문제가 없었다.
2. 어처피 합칠거, `join`말고 `reduce`를 쓰자. `map`을 처리 안하고,한번에 합칠 수 있다.
3. 문자열이 빈 문자열이어도 `false`, 140자를 넘어도 `false`면 로직을 합칠 수 있다.
   1. 문자열이 비어 있는 경우는 처리할 양도 적기 때문에 해쉬태그로 만드는 과정을 거친다고 하더라도
   성능에서 큰 손실을 보지는 않는다.

```js
const generateHashtag = (str) => {

  var hashtag = str.split(' ').reduce((acc, cur) =>
    acc + cur[0].toUpperCase() + cur.substring(1), '#'
  );
  
  return hashtag.length == 1 || hashtag.length > 140 ? false : hashtag;
} 
```

리턴이 없어서, 카멜케이스를 위해서 첫 글자를 바꾸는 로직은, 인덱스랑 substring을 활용했다.
