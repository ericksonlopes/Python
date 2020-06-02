from collections import defaultdict

l = defaultdict(list)

l['marcos'].append(10)
l['marcos'].append(12)
l['marcos'].append(154)

l['julio'].append(10)
l['julio'].append(77)

print(l)

s = defaultdict(set)

s['calus'].add(12)
s['calus'].add(127)

print(s)