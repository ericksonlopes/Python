frase = str(input('Digite uma frase: ')).upper().strip()

print(f'A letra A aparece {frase.count("A")} na frase')
print(f'A primeira letra A apareceu na posição {frase.find("A")}')
print(f'A ultima letra A apareceu na posição {frase.rfind("A")}')