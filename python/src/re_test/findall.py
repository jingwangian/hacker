#!/usr/bin/env python3

import re

s1 = 'http://www.hackerrank.com/'
m = re.findall(r'\w',s1)
print(m)

m1 = re.finditer(r'\w',s1)
[print(x.group(),end='-') for x in m1]

print('')
s2 = 'rabcdeefgyYhFjkIoomnpOeorteayeeeet'
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
m2 = re.findall(r'(?<=[%s])([%s]{2,})[%s]' %(c,v,c), s2, flags=re.I)
print(m2)