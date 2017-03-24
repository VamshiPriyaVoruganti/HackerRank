import re
for _ in range(int(raw_input())):
    color = "\n".join(re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})',raw_input()))
    if color!='': print(color)
