[print(item) for item in dir(open("demofile.txt"))]  # https://www.w3schools.com/python/python_ref_file.asp


with open("demofile3.txt", "a") as a:
    a.writelines(["See you soon!\n", "Over and out."])

with open("demofile3.txt", "r") as r:
    x = r.read().splitlines()

    for linha in range(len(x)):
        dado = x[linha].split('.')
        if len(dado) >= 2:
            remove = dado.pop(1)
        print(dado)


