const filePath =
  process.platform === 'linux'
    ? 'dev/stdin'
    : './input.txt';

const input = require('fs').readFileSync(filePath).toString().trim().split('\n');

const n = Number(input[0]);

const [A, B] = [input[1], input[3]].map(str => str.split(' ').map(Number));
A.sort((a, b) => a - b)

const binarySearch = (arr, target, start = 0, end = n - 1) => {
  while (start <= end) {
    const mid = Math.floor((start + end) / 2);
    
    if (arr[mid] === target) return 1;

    target > arr[mid]
      ? start = mid + 1
      : end = mid - 1;
  }
  return 0;
};

console.log(B.map(b => binarySearch(A, b)).join('\n'));


