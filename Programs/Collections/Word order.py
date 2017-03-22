from collections import OrderedDict
d = OrderedDict()
for _ in range(int(raw_input())): item = raw_input(); d[item] = d.get(item,0) + 1
print len(d)
for item, quantity in d.items():  print quantity,
