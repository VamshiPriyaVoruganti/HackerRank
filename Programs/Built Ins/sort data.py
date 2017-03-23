n, m = map(int, raw_input().split())
rows = [raw_input() for _ in range(n)]
k = int(raw_input())
for row in sorted(rows, key=lambda row: int(row.split()[k])): print(row)
