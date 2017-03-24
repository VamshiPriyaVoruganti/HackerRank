for _ in range(int(raw_input())): 
    s=raw_input()
    print "YES" if len(s)==10 and s.isdigit()  and (s[0]=='9' or s[0]=='8' or s[0]=='7') else "NO"
