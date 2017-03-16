def swap_case(s):
    s1=""
    for c in s:
        if c.islower():  
            c=c.upper()
        else:
            c=c.lower()
        s1+=c
    return s1
