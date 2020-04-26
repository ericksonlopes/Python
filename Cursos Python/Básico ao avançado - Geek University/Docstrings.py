"""
Documentando funções com docstirngs

OBS - Podemos   ter acesso á documentação de uma função em python
utilizando a propriedade especial __doc__.

Podemos ainda fazer acesso a documentação com a função 'help'
"""

# exemplos


def diz_oi():
    """Uma função simples qu retorna a string 'oi' """
    return 'oi'


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' á 'potência' informada
    :param numero: que desejamos gerar o exponencial
    :param potencia: potencia que queremos gerar o exponencial que por padrao é 2
    :return: retorna o exponencial de 'numero' por 'potencia'
    """
    return numero ** potencia


print(help(exponencial))
print(help(diz_oi))
