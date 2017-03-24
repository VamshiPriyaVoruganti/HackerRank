import re
s = '[qwrtypsdfghjklzxcvbnm]'
a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, raw_input(), re.I)
print('\n'.join(a or ['-1']))
