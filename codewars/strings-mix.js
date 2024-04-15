const alphabets = 'abcdefghijklmnopqrstuvwxyz'.split('');

const mix = (s1, s2) => {
  // 알파벳을 순회하면서 모든 문자열안에 모든 글자가 몇개 씩 들어있는지 센다.
  return alphabets
    .map(alphabet => {
      const
        s1Count = s1.split('').filter(letter => letter === alphabet).length,
        s2Count = s2.split('').filter(letter => letter === alphabet).length,
        maxCount = Math.max(s1Count, s2Count);

      return {
        letter: alphabet,
        count: maxCount,
        source: maxCount > s1Count ? '2'
          : maxCount > s2Count ? '1'
          : '='
      };
    })
    .filter(everyChar => everyChar.count > 1)  // 모든 문자얄에 몇개씩 받았는지 셌기 때문에, 문제 조건인 1번 초과 등장만 문자만 거른다
    .sort((objA, objB) => {
      objB.count - objA.count || (objA.source + objA.letter > objB.source + objB.letter ? 1 : -1)
    }) 
    .map(c => `${c.source}:${c.letter.repeat(c.count)}`)
    .join('/');
}
