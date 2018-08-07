#!/usr/bin/env python3

import numpy

a = numpy.array([1, 2, 3, 4, 5])

print(a[1])

b = numpy.array([1, 2, 3, 4, 5, 6], float)

print(b[::-1])

b.shape = (2, 3)
print(b[0], b[1])

[print(n) for row in b for n in row if n > 3]
