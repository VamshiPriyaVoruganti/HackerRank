from string import ascii_lowercase, ascii_uppercase 
sortkey = ascii_lowercase + ascii_uppercase + "1357902468"
print reduce(lambda x,y: x+y, sorted(raw_input(),key=sortkey.index))
