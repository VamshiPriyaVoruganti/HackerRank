if __name__ == '__main__':
    N = int(raw_input())
    l=[]
    y = ","
    for x in range(N):
        s= raw_input().split()
        value = s[0]
        value1= s[1:]
        if value!="print":
            value+="("+y.join(value1)+")"
            eval("l."+value)
        else:
            print(l)
