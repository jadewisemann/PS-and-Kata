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
  let chars = new Set(triplets.flat());
  let graph = {};
  let visited = {};
  let result = [];

  chars.forEach(char => {
    graph[char] = new Set();
    visited[char] = false;
  });

  triplets.forEach(triplet => {
    graph[triplet[0]].add(triplet[1]);
    graph[triplet[1]].add(triplet[2]);
  });

  function visit(char) {
    if (visited[char]) return;
    visited[char] = true;

    graph[char].forEach(nextChar => visit(nextChar));
    result.push(char);
  }

  chars.forEach(char => {
    if (!visited[char]) visit(char);
  });

  return result.reverse().join('');
}
