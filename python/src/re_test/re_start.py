#!/usr/bin/env python3

import re
s = 'abcd1234sfsfe'
m = re.search(r'\d+', s)
print(m.start(), m.end(), s[m.start():m.end()])


S = 'aaadaa'
k = 'aa'
pattern = re.compile(k)

r = pattern.search(S)

if not r:
    print("(-1,-1)")
while(r):
    print("({},{})".format(r.start(), r.end() - 1))
    r = pattern.search(S, r.start() + 1)
