for _ in range(int(raw_input())):
    l,lst=input(),map(int, raw_input().split()); i=0
    while i < l - 1 and lst[i] >= lst[i+1]:  i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:  i += 1
    print "Yes" if i == l - 1 else "No"
