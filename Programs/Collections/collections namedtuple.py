from collections import namedtuple
n, Student,total = input(), namedtuple('Student', raw_input()),0
for x in range(n): xyz=Student(*raw_input().split()); total+=int(xyz.MARKS)
print "%.2f" %(float(total)/int(n))
