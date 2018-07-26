#!/usr/bin/env python3

import re

mail_address = 'username@hackerrank.com.cn'

m = re.match(r'(\w+)@(\w+).(\w+)',mail_address)

print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))

print(m.groups())
print(m.groups()[0])
print(m.groups()[1])


m1 = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(\w+)','myname@hackerrank.com.cn')

# re.match(r'(?P<user>\w+)@(?P<website>\w+).(\w+)')
print(m1.groupdict())
print(m1.groups())

s1='..xx2x0312345678910111213141516171820212223'

m2 = re.search(r'([a-zA-Z0-9])\1+', s1)

print(m2.group(1) if m2 else -1)