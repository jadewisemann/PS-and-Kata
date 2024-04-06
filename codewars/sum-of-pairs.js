const sumPairs = (ints, s) => {
  const seen = {};
  for (let i = 0; i < ints.length; ++i) {
    if (seen[s - ints[i]]) return [s - ints[i], ints[i]];
    seen[ints[i]] = true
  }
};
