def merge_the_tools(string, k):
    n=len(string)
    for i in range(0,n,k):
        s=string[i:k+i]
        s1=""
        for x in range(len(s)):
            if s[x] in s1: pass
            else: s1+=s[x]
        print s1   
