x = [1, 1, 1, 1, 2, 5, 3, 4, 4, 4, 8, 8, 5, 6, 2, 1, 3, 2, 4, 5]

qt_ant = 0
moda = 0

for va in set(x):
    qt = 0
    for vb in x:
        if vb == va:
            qt += 1
    print(qt, va)



