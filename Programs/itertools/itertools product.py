from itertools import product
l=list(product(list(map(int, raw_input().split())),list(map(int, raw_input().split()))))
for x in l: print x,
