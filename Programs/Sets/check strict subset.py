s = set(map(int,raw_input().split()))
print(all(s > set(map(int,raw_input().split())) for _ in range(int(input()))))
