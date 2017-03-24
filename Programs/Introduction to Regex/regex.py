for _ in range(int(raw_input())):
    try:
        if float(raw_input()) != 0.0:
            print True
        else: print False
    except:
        print False
