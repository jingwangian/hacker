#!/usr/bin/env python3

# Nested Lists

"""
Input
~~~~~~~~
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39


output
~~~~~~~~
Berry
Harry


students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]


"""

if __name__ == '__main__':
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    # students = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())

    #     students.append([name, score])

    target_grade = sorted({s[1] for s in students})[1]
    satisfied_students = sorted([x[0] for x in students if x[1] == target_grade])
    [print(x) for x in satisfied_students]


d1 = 2.0

d2 = "{:.2f}".format(d1)

print(d2)
