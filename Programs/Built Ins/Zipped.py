n,m = map(int,raw_input().split())
z=zip(*[list(map(float,raw_input().split())) for _ in range(m)])
for x in z: print sum (marks for marks in x)/m
