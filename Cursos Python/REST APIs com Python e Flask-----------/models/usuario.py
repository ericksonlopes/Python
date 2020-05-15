from sql_alchemy import banco


# classe para criar o modelo de banco de dados
class UserModel(banco.Model):
    # nome da tabela
    __tablename__ = 'usuarios'
    # criando colunas do banco de dados
    id_user = banco.Column(banco.Integer, primary_key=True)
    login = banco.Column(banco.String(40))
    senha = banco.Column(banco.String(40))

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def json(self):
        return {
            'login': self.id_user,
            'senha': self.senha
        }

    @classmethod
    def find_user(cls, id_user):
        # faz uma query no banco de dados, selecionado o primeiro encotrado com essa
        user = cls.query.filter_by(id_user=id_user).first()
        # verifica se encontrou algum item
        if user:
            # retorna o hotel encontrado
            return user
        # se não encontrar retorna nome
        return None

    @classmethod
    def find_by_user(cls, login):
        # faz uma query no banco de dados, selecionado o primeiro encotrado com essa
        user = cls.query.filter_by(login=login).first()
        # verifica se encontrou algum item
        if user:
            # retorna o hotel encontrado
            return user
        # se não encontrar retorna nome
        return None

    def save_user(self):
        # adiciona os itens no banco de dados
        banco.session.add(self)
        banco.session.commit()

    def delete_user(self):
        banco.session.delete(self)
        banco.session.commit()

