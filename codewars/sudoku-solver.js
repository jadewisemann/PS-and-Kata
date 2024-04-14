/*

```yaml
problem: "Sudoku Solver"
tags: game, game-solver, algorithm
difficulty: 3-kyu
source: codewars
link: https://www.codewars.com/kata/5296bc77afba8baa690002d7
```

Write a function that will solve a 9x9 Sudoku puzzle.
The function will take one argument consisting of the 2D puzzle array,
with the value `0` representing an unknown square.

The Sudokus tested against your function will be "easy"
(i.e. determinable; there will be no need to assume and test possibilities on unknowns)
and can be solved with a brute-force approach.

For Sudoku rules, see [the Wikipedia article](http://en.wikipedia.org/wiki/Sudoku).

```javascript
var puzzle = [ 
  [5,3,0,0,7,0,0,0,0],
  [6,0,0,1,9,5,0,0,0], 
  [0,9,8,0,0,0,0,6,0], 
  [8,0,0,0,6,0,0,0,3], 
  [4,0,0,8,0,3,0,0,1], 
  [7,0,0,0,2,0,0,0,6], 
  [0,6,0,0,0,0,2,8,0], 
  [0,0,0,4,1,9,0,0,5], 
  [0,0,0,0,8,0,0,7,9]
]; 

sudoku(puzzle);
/* Should return [
  [5,3,4,6,7,8,9,1,2], 
  [6,7,2,1,9,5,3,4,8], 
  [1,9,8,3,4,2,5,6,7], 
  [8,5,9,7,6,1,4,2,3], 
  [4,2,6,8,5,3,7,9,1], 
  [7,1,3,9,2,4,8,5,6], 
  [9,6,1,5,3,7,2,8,4], 
  [2,8,7,4,1,9,6,3,5], 
  [3,4,5,2,8,6,1,7,9]
]
```
*/



const sudoku = puzzle => {
  // 변수 선언 :  
  const
    rows = new Array(9).fill(0),
    cols = new Array(9).fill(0),
    boxes = new Array(9).fill(0);
  // 모든 퍼즐 순회ㅣ,
  for (let row = 0; row < 9; row++) {
    for (let col = 0; col < 9; col++) {
      const num = puzzle[row][col];
      if (num !== 0) {
        const mask = 1 << (num - 1);
        rows[row] |= mask;
        cols[col] |= mask;
        boxes[Math.floor(row / 3) * 3 + Math.floor(col / 3)] |= mask;
      }
    }
  }

  const isValid = (row, col, num) => {
    const mask = 1 << (num - 1);
    return !(rows[row] & mask || cols[col] & mask || boxes[Math.floor(row / 3) * 3 + Math.floor(col / 3)] & mask);
  };

  const setNumber = (row, col, num, add) => {
    const mask = 1 << (num - 1);
    rows[row] = add ? rows[row] | mask : rows[row] & ~mask;
    cols[col] = add ? cols[col] | mask : cols[col] & ~mask;
    boxes[Math.floor(row / 3) * 3 + Math.floor(col / 3)] = add ? boxes[Math.floor(row / 3) * 3 + Math.floor(col / 3)] | mask : boxes[Math.floor(row / 3) * 3 + Math.floor(col / 3)] & ~mask;
  };

  const solve = () => {
    let minOptions = 10, rowToFill = -1, colToFill = -1;
    for (let row = 0; row < 9; row++) {
      for (let col = 0; col < 9; col++) {
        if (puzzle[row][col] === 0) {
          let options = 0;
          for (let num = 1; num <= 9; num++) {
            if (isValid(row, col, num)) options++;
          }
          if (options < minOptions) {
            minOptions = options;
            rowToFill = row;
            colToFill = col;
          }
        }
      }
    }

    if (minOptions === 10) return true; // Solved

    for (let num = 1; num <= 9; num++) {
      if (isValid(rowToFill, colToFill, num)) {
        puzzle[rowToFill][colToFill] = num;
        setNumber(rowToFill, colToFill, num, true);
        if (solve()) return true;
        setNumber(rowToFill, colToFill, num, false);
        puzzle[rowToFill][colToFill] = 0;
      }
    }

    return false;
  };

  solve();
  return puzzle;
};
