for _ in range(int(raw_input())):
    try:
        a,b=map(int,raw_input().split())
        print a//b
    except Exception as e:
        print "Error Code:",e
