const sudoku = puzzle => {

  const isValid = (row, col, num) => {
    for (let i = 0; i < 9; i++) if (puzzle[row][i] === num || puzzle[i][col] === num) return false;

    const startRow = Math.floor(row / 3) * 3;
    const startCol = Math.floor(col / 3) * 3;
    
    for (let i = 0; i < 3; i++)
      for (let j = 0; j < 3; j++)
        if (puzzle[startRow + i][startCol + j] === num) return false;
    return true;
  };

  const solve = () => {
    for (let row = 0; row < 9; row++)
      for (let col = 0; col < 9; col++) {
        if (puzzle[row][col] === 0) {
          for (let num = 1; num <= 9; num++)
            if (isValid(row, col, num)) {
              puzzle[row][col] = num;
              if (solve()) return true;
              puzzle[row][col] = 0
            };
          return false;
        }
      }
    return true;
  };

  solve();
  return puzzle;
};
