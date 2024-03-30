const toCamelCase = str => str
  .split(/_|-/)
  .map((word, idx) => idx === 0 ? word : word[0].toUpperCase() + word.slice(1))
  .join('')
