const brainLuck = (code, input) => {
  var data = [],
      dataPointer  = 0,
      inputPointer = 0,
      output = [],
      skipping = 0,
      backwards = 0;

  var COMMANDS = {
    '>': () => ++dataPointer ,
    '<': () => --dataPointer,
    '+': () => data[dataPointer] = ((data[dataPointer] || 0) + 1) % 256,
    '-': () => data[dataPointer] = ((data[dataPointer] || 0) + 255) % 256,
    '.': () => output.push(data[dataPointer]),
    ',': () => data[dataPointer] = (input[inputPointer++] || '').charCodeAt(),
    '[': () => (!data[dataPointer]) &&  (skipping = 1),
    ']': () => (data[dataPointer]) && ( backwards = 1) 
  };

  for (var currentPointer = 0; currentPointer <= code.length; ++currentPointer) {
    skipping ? (
      (code[currentPointer] === '[') && (skipping++),
      (code[currentPointer] === ']') && (skipping--))
    : backwards ? (
      currentPointer -= 2,
      (code[currentPointer] === ']') && (backwards++),
      (code[currentPointer] === '[') && (backwards--))
    : code[currentPointer] &&
      COMMANDS[code[currentPointer]]();
  }

  return String.fromCharCode.apply(null, output)
}