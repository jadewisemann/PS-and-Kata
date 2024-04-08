const mix = (s1, s2) => {

  const getFrequencyMap = str =>
    [...str]
      .filter(char => char >= 'a' && char <= 'z')
      .reduce((acc, char) => {
        acc[char] = (acc[char] || 0) + 1;
        return acc;
      }, {});

  const freqMap1 = getFrequencyMap(s1);
  const freqMap2 = getFrequencyMap(s2);

  const allKeys = new Set([...Object.keys(freqMap1), ...Object.keys(freqMap2)]);

  let result = [...allKeys]
    .reduce((acc, key) => {
      const count1 = freqMap1[key] || 0;
      const count2 = freqMap2[key] || 0;

      if (count1 > 1 || count2 > 1) {
        const prefix = count1 > count2 ? '1' : count1 < count2 ? '2' : '=';
        acc.push(`${prefix}:${key.repeat(Math.max(count1, count2))}`);
      }

      return acc;
    }, [])
    .sort((a, b) => {
      const lengthDifference = b.slice(3).length - a.slice(3).length;
      if (lengthDifference !== 0) return lengthDifference;

      const priority = {'1': 1, '2': 2, '=': 3};
      const prefixOrder = priority[a[0]] - priority[b[0]];

      return prefixOrder !== 0 ? prefixOrder : a.localeCompare(b);
    });

  return result.join('/');
}
