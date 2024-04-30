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
  const trimmedStr = str.trim();
  if (!trimmedStr) return false;

  const hashtag = `#${trimmedStr
    .split(/\s+/)
    .map(word => word.replace(/^\S/, c => c.toUpperCase()))
    .join('')}`;
  
  return hashtag.length > 140 ? false : hashtag;
};
