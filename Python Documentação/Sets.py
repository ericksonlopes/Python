# Tudo sobre Sets
# = {1, 2, 23}

for item in dir(set):
    print(item)
print()

# Ele não duplica
# Você não pode alterar itens

# # Acesso dados
# set_ = {1, 2, 4, 3, 3, 3, 3, 3, 3, 3}
# print(set_)

# # verificar se existe um item
# set_ = {1, 2, 4, 3, 3, 3, 3, 3, 3, 3}
# print(3 in set_)

# # adicionar itens
# set_ = {1, 2, 4, 3, 3, 3, 3, 3, 3, 3}
# set_.add(7)
# print(set_)

# # apagar tudo em set
# set_ = {1, 2, 4, 3, 3, 3, 3, 3, 3, 3}
# set_.clear()
# print(set_)

# # Copiar o set
# set_ = {1, 2, 4, 3, 3, 3, 3, 3, 3, 3}
# set_copia = set_.copy()

# # Para remover um item de um conjunto, use o método remove() ou discard()
# set_ = {1, 2, 4, 3, 3, 3, 3, 3, 3, 3}
# set_.remove(3)
# print(set_)
# # ou
# set_ = {1, 2, 4, 3, 3, 3, 3, 3, 3, 3}
# set_.discard(3)
# print(set_)

# # remover e retornar o item que estiver na posição 0
# set_ = {1, 2, 4, 3, 3, 3, 3, 3, 3, 3}
# removido = set_.pop()
# print(removido)

# # unir dois conjuntos
# set1 = {1, 2, 3}
# set2 = {'a', 'b', 'c'}
# print(set1.union(set2))

# # inserir itens set2 no set 1
# set1 = {1, 2, 3}
# set2 = {'a', 'b', 'c'}
#
# set1.update(set2)


# # Retorna um conjunto contendo a diferença entre dois ou mais conjuntos
# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5, 6}
#
# print(set2.difference(set1))

# # Remova os itens que existem nos dois conjuntos:
# set1 = {1, 2, 3, 4, 5, 7}
# set2 = {'a', 'b', 'c', 4, 5, 7}
#
# set1.difference_update(set2)
#
# print(set1)
# print(set2)

# # Retorna um conjunto, que é a interseção de outros dois conjuntos
# set1 = {1, 2, 3, 4, 5, 7}
# set2 = {'a', 'b', 'c', 4, 5, 7}
#
# set3 = set1.intersection(set2)
# print(set3)

# # Remove do set os valores que nao estao presentes em ambos
# set1 = {1, 2, 3, 4, 5, 7}
# set2 = {'a', 'b', 'c', 4, 5, 7}
#
# set2.intersection_update(set1)
#
# print(set1)
# print(set2)

# # Retorne True se nenhum item no conjunto x estiver presente no conjunto y :
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "facebook"}
#
# z = x.isdisjoint(y)
#
# print(z)

# # Retorne True se todos os itens do conjunto x estiverem presentes no conjunto y :
# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}
#
# z = x.issubset(y)
#
# print(z)

# # Retorne True se todos os itens definidos y estiverem presentes no conjunto x :
# x = {"f", "e", "d", "c", "b", "a"}
# y = {"a", "b", "c"}
#
# z = x.issuperset(y)
#
# print(z)

# # Retorne um conjunto que contém todos os itens dos dois conjuntos, exceto os itens presentes nos dois conjuntos:
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
#
# z = x.symmetric_difference(y)
#
# print(z)

# Remova os itens presentes nos dois conjuntos E insira os itens que não estão presentes nos dois conjuntos:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
