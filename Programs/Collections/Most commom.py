from collections import Counter
s = input().strip()
c = Counter(s).most_common()
for element in sorted(c, key=lambda x: (-x[1], x[0]))[:3]:
    print(" ".join(str(e) for e in element), sep=" ")
