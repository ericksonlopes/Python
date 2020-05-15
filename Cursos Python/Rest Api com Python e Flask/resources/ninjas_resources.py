from flask_restful import Resource, reqparse

# dados temporários
ninjas = [
    {'id_nome': 'Madara Uchiha',
     'altura': 1.80,
     'cla': 'Uchiha'},
    {'id_nome': 'Naruto Uzumaki',
     'altura': 1.75,
     'cla': 'Uzumaki'}
]


# classe que retorna todos os dados
class Ninjas(Resource):
    # quando a requisição get for passada executa essa função
    def get(self):
        return {'Ninjas': ninjas}


# classe que realiza o crud em cada item
class Ninja(Resource):
    # Pega os dados recebidos do usuario através das chaves e definindo construtor
    argumentos = reqparse.RequestParser()
    # procura a chave que tenha o valor "altura"
    argumentos.add_argument('altura')
    argumentos.add_argument('cla')

    # função que procura o item
    def find_ninja(self, id_nome):
        # percore a lista ninja
        for item in ninjas:
            # verifica se a chave de id é equiválente
            if item['id_nome'] == id_nome:
                # retorna o item se encontrar
                return item
        # Retorna None se não encontrar equiválente
        return None

    # função que busca pelo id_nome
    def get(self, id_nome):
        encontrado = self.find_ninja(id_nome)
        # se encontrado não for None(nulo)
        if encontrado is not None:
            # retorna o item encontrado
            return encontrado

        # caso não encontre, retorna essa mensagem
        return {'message': 'Ninja not found'}, 404  # não encontrado

    def post(self, id_nome):
        # compacta os itens enviados em chave e valor criando um dicionario(dados)
        dados = Ninja.argumentos.parse_args()

        # criando um novo ninja com os dados recebidos do usuario
        novo_ninja = {
            # o id_nome ja é passado pelo usuario na requisição
            'id_nome': id_nome, **dados}

        ninjas.append(novo_ninja)
        return novo_ninja, 200  # realizado com sucesso

    def put(self, id_nome):
        # verifica se o id_nome existe
        ninja = self.find_ninja(id_nome)

        # Recebe os itens do construtor
        dados = Ninja.argumentos.parse_args()
        # cria um novo com os itens recebido do usuario com o id_nome
        novo_item = {'id_nome': id_nome, **dados}

        # se o item existir
        if ninja:
            # com uma função built-in atualiza os dados do dicionario com o recebido
            ninja.update(novo_item)
            return novo_item, 201

        #
        ninjas.append(novo_item)
        return novo_item, 200

    def delete(self, id_nome):
        # Global significa que a lista aplica aqui dentro
        global ninjas
        # ja que estamos útilizando uma lista, imprimimos todos os valores tirando o valor com o id_referente
        ninjas = [ninja for ninja in ninjas if ninja['id_nome'] != id_nome]
        return {'message': 'Ninja deleted'}
