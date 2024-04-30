

### [kata][5-kyu][.js] Pete, the baker ( TIL 24 04 30 )

```yaml
problem: 'Pete, the baker'
tags: ALGORITHMS
difficulty: 5-kyu
source: codewars
link: https://www.codewars.com/kata/525c65e51bf619685c000059
```

# problem

`recipe`, `available` , 두 개의  객체를 받는다.
레시피에 나온 빵은 만든다고 했을때, 가지고 있는 가용량으로 몇개를 만들 수 있는지 반환하라.

# 🤔

모든 재료에 대해서 각각의 가용량으로 몇개를 만들 수 있는지 따로 구한 후에,가장 작은 양이 정답이다.
가장 적은량이 몇개를 만들지 결정하기 때문이다.

두가지 주의점이 있다.
- `available`에 아예 없는 경우.
  - 부족한 경우에는 상관 없지만, 재고가 아예없어서 키도 없는 경우, 객체에 `key`를 조회하면,
  `undefined`를 반환한다.
- `Math.min()`은 이터러블한 객체의 값을 자동으로 추출해서 비교하지 않는다
  
이 두가지만 조심해서 작성하면 될 것이다.

## solution #1

```js
const  cakes = (recipe, available) => {
  const minArr = []
  Object.entries(recipe).forEach( ([key, value]) => {
    minArr.push(Math.floor((available[key] ? available[key] : 0) / value))
  })
  return Math.min(...minArr)
}
```

`Object.entries`를 이용해서 키 벨류를 한번에 조회하는 방식을 사용했다.
`minArr`를 선언해서, 최소값을 저장하고, 최소값을 spread syntax를 사용해서 늘어 놓고, `Math.min`으로 최소값을 반환했다.
삼항 연산자를 사용해서 키가 없으면 0을 반환하도록 만들었다.

## solution #1.1 (refactoring)

1. 그런데 생각해보면, 어처피 반환값은 `Math.min`의 반환값이다.
```js
const  cakes = (recipe, available) => Math.min( ~~~ )
```
이런 식으로 좀 더 간결하게 할 수 있다.

2. `minArr`도 저장했다가 바로 분해 되기 때문에, 차라리 지정하지 말고, 고차함수로 결과값을 바로 `Math.min`에 할당해 주자.
```js
const  cakes = (recipe, available) => Math.min(
  ... Object.entries(recipe).forEach(([key, value]) => Math.floor((available[key] ? available[key] : 0) / value))
)
```

3. `forEach`를 전에 사용한 이유는 값 자체를 반환하지 않고, 외부 객체에 값을 저장했기 때문이다.
하지만, 함수안의 함수로서 결과를 바로 반환하여 `Math.min`에 넘겨 주어야 하므로 `return`을 하는 `Array.prototype.map()`을 사용하자.
```js
const  cakes = (recipe, available) => Math.min(
  ... Object.entries(recipe).map(([key, value]) => Math.floor((available[key] ? available[key] : 0) / value))
)
```

4. `undefined`를 나눈다고 에러가 발생하지는 않는다. 중복을 줄이기 위해서 `||`를 사용하자.
```js
const cakes = (recipe, available) => Math.min(
  ...Object.entries(recipe).map(([key, value]) => Math.floor((available[key] / value) || 0))
)
```

> #### `undefined` 와 `NaN` 
> `undefined`를 나누면, `NaN`이 나온다.
>숫자가 아닌걸 숫자처럼 다뤘기 때문에 `Not A Number`가 나오는 것이다.
>
>`NaN`은 `falsy`한 값이기 때문에, 나눔의 결과가 `NaN`이면
>  (`available[key]`가 `undefined`라는 뜻)
>`||`가 뒤의 값을 반환한다.


