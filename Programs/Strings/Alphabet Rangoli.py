import string
def print_rangoli(size):
    alpha = string.ascii_lowercase
    for i in range(size,1,-1):
        s = "-".join(alpha[i-1:size])
        s=((s[::-1]+s[1:]).center(4*size-3, "-"))
        print s
    for i in range(size):
        s = "-".join(alpha[i:size])
        s=((s[::-1]+s[1:]).center(4*size-3, "-"))
        print s
