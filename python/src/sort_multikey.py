#!/usr/bin/env python3
from operator import itemgetter, attrgetter

a = [('Abel', 3), ('Zeke', 2), ('Chris', 1),('Al', 2),('Carol', 2),('Bill', 1)]

# sort by 2nd element and then 1st element 
b = sorted(a, key = lambda x : (x[1], x[0]))

#or b = sorted(a, key = itemgetter(1,0))
#or b = sorted(a, key = attrgetter(1,0))

[print(x) for x in b]
"""
'Bill', 1)
('Chris', 1)
('Al', 2)
('Carol', 2)
('Zeke', 2)
('Abel', 3)
"""

## sort by 2nd element ascend and then 1st element descend
c = sorted(a, key = itemgetter(0), reverse=True)
c = sorted(c, key = itemgetter(1))

print(c)