"""
módulos Externos

Utilizamos o gerenciador de pacotes Python  chamnado pip

"""

# # chamando o pacote e retirando sua função
# from geek import geek1
#
# print(geek1.funcao(5, 6))

# chamando pacote dentro de pacote
from geek.university import geek3

print(geek3.funcao(2, 7))
