# -*- coding: utf-8 -*-
"""
POO - Métodos

O __init__ é um método especial chamado de construtor e sua função é construir o objeto a partir da classe

métodos são criados em letras minusculas
"""
# importnato biblioteca de criptografia para senhas
from passlib.hash import pbkdf2_sha256 as cryp


class Produto:
    # Atributo de classe
    imposto = 0.05
    contador = 0

    def __init__(self, valor, senha):
        self.__senha = cryp.encrypt(senha, rounds=200000, salt_size=16)
        self.id = Produto.contador + 1
        self.__valor = valor
        Produto.contador = self.id

    def exibir_valor(self):
        print(self.__valor)
        print(self.id)

    def desconto(self, porcentagem):
        """Retorna o valor do produto"""
        return self.__valor * (100 - porcentagem) / 100

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


v1 = Produto(100, 147258369)
print(v1.desconto(50))
print(v1.checa_senha(147258369))
