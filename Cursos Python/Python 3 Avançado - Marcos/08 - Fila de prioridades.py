import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    # adiciona item na lista
    def push(self, item, priority):
        # -priority ( para fica rdo maior para o menor)
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    # remove um item da lista
    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


q = PriorityQueue()
lista = [['joao', 1], ['sim', 11]]
q.push(lista[0][0], lista[0][1])
q.push(lista[1][0], lista[1][1])
# q.push(Person('Erickson'), 19)
# q.push(Person('joao'), 30)
# q.push(Person('calaoira'), 17)

# retorna o a pessoa com maior número na idade
print(q.pop())
