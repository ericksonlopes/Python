import platform

sistema_usado = platform.system()
print('Sistema: Windows' if sistema_usado == 'Windows' else 'Você não esta usando Windows')

sistema_versao = platform.version()
print('versão: ' + sistema_versao)

sistema_processador = platform.processor()
print('Processador: ' + sistema_processador)

sistema_node = platform.node()
print('Node: ' + sistema_node + '\n')

# exibe as funções sem os inicializadores (__palavra__)
s = dir(platform)
for funcao in s:
    if funcao[0] != '_':
        print(funcao)


# importar função escolhida
from funcoes_que_eu_criei import adicionar as add

print(add(10, 20))
