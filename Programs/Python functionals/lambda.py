cube = lambda x: pow(x,3) # complete the lambda function 
def fibonacci(n):
    a=0;b=1;l=[]
    if n>0:
        l.append(a)
        if n>1:
            l.append(b)
            for x in range(n-2):
                c=a+b
                l.append(c)
                a=b
                b=c
    return l
    # return a list of fibonacci numbers
