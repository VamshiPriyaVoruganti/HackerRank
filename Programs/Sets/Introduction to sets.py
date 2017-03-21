def average(array):
    a={}
    a=set()
    for x in range(len(array)):
        a.add(array[x])
    return sum(a)/len(a)
