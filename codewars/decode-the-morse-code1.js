const decodeMorse = morseCode => { 
  const decodeMorseLetter = letter => MORSE_CODE[letter] || ""
  const decodeMorseWord = word => word.split(' ').map(decodeMorseLetter).join('');
  return morseCode.trim().split('   ').map(decodeMorseWord).join(' ');
}