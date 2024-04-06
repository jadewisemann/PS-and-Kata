const sumPairs = (ints, s) => {
  const seen = {};
  for (let int of ints) {
    if (seen[s - int]) return [s - int, int];
    seen[int] = true
  }
};
