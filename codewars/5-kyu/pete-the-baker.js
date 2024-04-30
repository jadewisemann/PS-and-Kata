/*
```yaml
problem: 'Pete, the baker'
tags: ALGORITHMS
difficulty: 5-kyu
source: codewars
link: https://www.codewars.com/kata/525c65e51bf619685c000059
```
*/

const  cakes = (recipe, available) => {
  const minArr = []
  Object.entries(recipe).forEach( ([key, value]) => {
    minArr.push(Math.floor((available[key] ? available[key] : 0) / value))
  })
  return Math.min(...minArr)
}

