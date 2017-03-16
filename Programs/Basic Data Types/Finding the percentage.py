if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    l=student_marks[query_name]
    sum=0
    for x in range(len(l)):
        sum+=l[x]
    print ("%.2f" %(sum/3))
