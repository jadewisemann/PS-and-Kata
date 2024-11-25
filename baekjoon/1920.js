const filePath =
  process.platform === 'linux'
    ? 'dev/stdin'
    : './input.txt';

const input = require('fs').readFileSync(filePath).toString().trim().split('\n');

const [A, B] = [input[1], input[3]].map(str => str.split(' ').map(Number));
A.sort((a, b) => a - b)

const aArr = new Set(A);
const answer = B.map( b => aArr.has(b) ? 1 : 0);
console.log(answer.join('\n'))

