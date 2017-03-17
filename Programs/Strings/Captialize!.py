def capitalize(string):
    string1=""
    for x in range(len(string)):
        if x==0: string1+=string[x].upper()
        elif string[x]==" ":  
            string1+=string[x]
            if string[x+1]!=" ":
                string1+=string[x+1].upper()
            x+=1
        elif string[x-1]!=" ":  string1+=string[x]
    return string1


