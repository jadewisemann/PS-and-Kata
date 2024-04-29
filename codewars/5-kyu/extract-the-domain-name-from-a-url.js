const domainName = url => url
  .replace('https://', '')
  .replace('http://', '')
  .replace('www.', '')
  .split('/')[0]
  .split('.')[0]
