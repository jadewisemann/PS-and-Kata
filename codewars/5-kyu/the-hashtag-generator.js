/*
```yaml
problem: 'The Hashtag Generator'
tags: STRINGS, ALGORITHMS
difficulty: 5-kyu
source: codewars
link: https://www.codewars.com/kata/52449b062fb80683ec000024
```
*/

const generateHashtag = (str) => {

  var hashtag = str.split(' ').reduce((acc, curr) =>
    acc + curr[0].toUpperCase() + curr.substring(1), '#'
  );
  
  return hashtag.length == 1 || hashtag.length > 140 ? false : hashtag;
}