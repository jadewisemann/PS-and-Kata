order = words => !words ? words : words
  .split(' ')
  .sort((a, b) => a.match(/\d/) - b.match(/\d/))
  .join(' ');

console.log(newOrder("is2 Thi1s T4est 3a"))