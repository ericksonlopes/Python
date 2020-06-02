from collections import Counter

c = Counter(a=4, b=2, c=3)

print(list(c.elements()))

# elementos mais comuns
print(c.most_common())

print(c.most_common(2))