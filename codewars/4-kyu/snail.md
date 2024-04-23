```yaml
problem: 'Snail'
tags: ARRAYS, ALGORITHMS
difficulty: 4-kyu
source: codewars
link: https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
```


# problem : Snail

정사각형 어레이가 주어진다.

```js
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
```

```js
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
```
이렇게 출력하라.

# 🤔

이거 인덱스를 하나 하나 이동해도 되기야 하겠지만
개인적으로 인덱스 이동이 싫다!
그냥 싫다 이거야!

그래서 세이프하게 그냥 전체 배열을 몇번씩 순회하는 방법을 생각했다.

## solution 1

```js
const snail = array => {
  var result = [];
  while (array.length) {
    // 상단
    result = [...result, ...array.shift()];
    // 우측
    array.forEach(row => {
      result.push(row.pop());
    });
    // 하단
    if (array.length) {
      result = [...result, ...array.pop().reverse()];
    }
    // 좌측
    array.slice().reverse().forEach(row => {
      result.push(row.shift());
    });
  }
  return result;
}
```


### use while

`while`문으로 순회를 한다.

> 파이선이랑 다르게 `js`에서 빈배열은 truthy다. `while (array.length)` 에서
> 파이선 처럼 `array`만 잡으면 `while`은 계속 돈다.

### 가장 윗줄 추가

가장 윗줄을 추가한다.

```js
    result = [...result, ...array.shift()];
```

### 오른쪽 추가

`forEach`로 순회하면서 오른쪽 요소를 추가해준다.
반환값이 필요없으면 굳이 `map`을 사용할 필요는 없다.

```js
    array.forEach(row => {
      result.push(row.pop());
    });
```

### 반대로 처리하기

여기서 부터는 끝줄과 왼쪽 인데 동일한 동작을 한다.
다만 방향의 변화를 구현하기 위해, `reverse`, `shift`대신 `pop` 등을 사용하는 등의 차이만 있다.

>왼쪽을 처리할때는 범위 없는 `slice`를 걸어줘서, 복사본을 만든후, 역방향을 순회하는데 이는 원본을 변형하는 것을 막기 위함이다

### 홀수 처리하기

밑 줄을 처리 할때 보면,
while문에 조건이 잡혀 있긴 하지만 중간에 한번더  `if (array.length)` 가 있다.

홀수의 경우, 마지막에는 위, 우측을 처리하고 나면 배열이 비어버린다.
좌측을 처리하는 메소드는 괜찮지만 하단을 처리하는 `pop`은 빈배열에 하면 오류가 나기때문에 `if`문으로 홀수 마지막에 빈배열에 동작하지 않도록 거러주자

## refactor

사실 이게 워낙 마음에 안든게.
중복 로직이 많다.

거의 동일한 로직을 방향만 바꿔서 두번을 하고 있으니 마음에 들리가 없다.
이걸 줄일 방법은 단 한가지 방법을 생각했는데,
위 우측만 처리하고, 상하좌우를 뒤집는 것이다.

이 경우, 홀수 처리도 생각할 필요가 없는 것이, `pop`이 있는 상, 하 처리가 한번에 이뤄저서 홀수에 문제가 생긴 것인데
한번씩 `pop`하고 뒤집고 하면 `if`문도 간결하게 처리가 가능하다.

```js
const snail = array => {
  var result = [];
  while (array.length) {
    result = [...result, ...array.shift()]
    array.forEach(row => result.push(row.pop()))
    array.reverse().forEach(row => row.reverse());
  }
  return result;
}
```

이렇게 하면 몇 배는 간결하게처리가 가능하다.


# review : 😆

이거, 간만에 생각할거 좀 있고 재미있었던거 같다.

사실 결과물이 마음에 들어서 마음에 든다.
그런데 가장 클래버한 케이스에 거의 비슷한 코드가 있어서 좀,,, 마음이 애리긴하다,,,

#


######