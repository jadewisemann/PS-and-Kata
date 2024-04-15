const solution = (list) => {
  const result = [];

  for (let i = 0; i < list.length; i++) {
    let start = list[i];

    while (list[i + 1] - list[i] === 1) {
      i++;
    }
    let end = list[i];

    if (start === end) {
      result.push(`${start}`);
    } else if (end - start === 1) {
      result.push(`${start}`, `${end}`);
    } else {
      result.push(`${start}-${end}`);
    }
  }

  return result.join(',');
};
