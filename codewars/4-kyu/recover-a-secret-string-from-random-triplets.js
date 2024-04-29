/*

```yaml
problem: "Recover a secret string from random triplets"
tags: algorithms
difficulty: 4-kyu
source: codewars
link: https://www.codewars.com/kata/53f40dff5f9d31b813000774
```
*/


const recoverSecret = triplets => {
  const graph = {};
  const visited = {};
  const result = [];

  triplets.flat().forEach(char => {
    graph[char] = new Set();
    visited[char] = false;
  });

  triplets.forEach(([first, second, third]) => {
    graph[first].add(second);
    graph[second].add(third);
  });


  const visit = char => {

    if (visited[char]) return;
    visited[char] = true;

    graph[char].forEach(visit);
    result.push(char);
  };

  Object.keys(graph).forEach(char => {
    if (!visited[char]) visit(char);
  });

  return result.reverse().join('');
};

triplets1 = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]
console.log(recoverSecret(triplets1))
