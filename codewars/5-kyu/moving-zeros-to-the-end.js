function moveZeros(arr) {
    return [
      ...arr.filter(item => item !== 0),
      ...arr.filter(item => item === 0)
    ];
}