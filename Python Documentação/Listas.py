# Tudo sobre Listas
# list1 = ['physics', 'chemistry', 1997, 2000];

for item in dir(list):
    print(item)
print()

# # criar a lista
# lista = []

# # Acessar o valor
# lista = [1, 2, 3, 4]
# print(lista[1])

# # adicionar elemento na lista
# valor = 5
# lista.append(valor)
# print(lista)

# # prolongar a lista
# lista1 = [1, 2]
# lista2 = [3, 4]
#
# lista1.extend(lista2)
# print(lista1)

# # remover item de uma lista
# lista = [1, 5, 2, 3]
# lista.remove(5)
# print(lista)

# # Remove um item em uma dada posição na lista e o retorna
# lista = [1, 5, 2, 3]
# retorna = lista.pop(1)
# print(retorna)

# # Remove todos os itens de uma lista
# lista = [1, 5, 2, 3]
# lista.clear()
# print(lista)

# # Devolve o índice base-zero do primeiro item cujo valor é igual a x
# lista = [1, 3]
# lista.insert(1, 'Dois')
# print(lista)

# # Devolve o número de vezes em que x aparece na lista.
# lista = [1, 2, 3, 4, 4, 4, 6, 7, 8, 9, 5]
# num_vezes = lista.count(4)
# print(num_vezes)

# # Ordena os itens na list
# lista = [1, 4, 6, 8, 7, 9]
# lista.sort(reverse=True)
# print(lista)

# # Devolve uma cópia rasa da lista
# lista = [1, 2, 3, 4]
# lista_copia = lista.copy()
# print(lista_copia)

# # Retorna o index onde o elemento está
# lista = [1, 2, 3, 4]
# print(lista.index(4))
# print(lista)

# # trnsformar em lista um iteravel
# palavra = 'xzy'
# print(list(palavra))

# Verificar se existe o item na lista
lista = [1, 2, 3, 4]
print(2 in lista)

