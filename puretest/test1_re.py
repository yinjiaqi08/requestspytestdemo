import re
text = 'abc"origin": "1.23.45.678"def'
print(re.search('"origin": "(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})"', text).group(1))