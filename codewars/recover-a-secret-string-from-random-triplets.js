/*

```yaml
problem: "Recover a secret string from random triplets"
tags: algorithms
difficulty: 4-kyu
source: codewars
link: https://www.codewars.com/kata/53f40dff5f9d31b813000774
```

There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.

A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string.
"whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the secret string.

You can assume nothing about the triplets given to you other than that they are valid triplets
and that they contain sufficient information to deduce the original string.
In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.
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
