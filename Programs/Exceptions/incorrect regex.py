import re
for _ in range(int(raw_input())):
    try:
        re.compile(raw_input())
        print True
    except re.error:
        print False
