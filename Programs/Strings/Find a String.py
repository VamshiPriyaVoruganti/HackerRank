def count_substring(string, sub_string):
    count=0
    length=len(sub_string)
    for x in range(len(string)):
        if x+1<len(string)-1:
            match=string[x:length+x]
            if match==sub_string:
                count+=1       
    return count
