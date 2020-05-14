from sql_alchemy import banco


# classe para criar o modelo de banco de dados
class HotelModel(banco.Model):
    # nome da tabela
    __tablename__ = 'hoteis'
    # criando colunas do banco de dados
    id_hotel = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String())
    estrelas = banco.Column(banco.Float(precision=1))
    diaria = banco.Column(banco.Float(precision=2))
    cidade = banco.Column(banco.String(40))

    def __init__(self, id_hotel, nome, estrelas, diaria, cidade):
        self.id_hotel = id_hotel
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def json(self):
        return {
            'id_hotel': self.id_hotel,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
        }

    @classmethod
    def find_hotel(cls, id_hotel):
        # faz uma query no banco de dados, selecionado o primeiro encotrado com essa
        hotel = cls.query.filter_by(id_hotel=id_hotel).first()
        # verifica se encontrou algum item
        if hotel:
            # retorna o hotel encontrado
            return hotel
        # se não encontrar retorna nome
        return None

    def save_hotel(self):
        # adiciona os itens no banco de dados
        banco.session.add(self)
        banco.session.commit()

    def update_hotel(self, nome, estrelas, diaria, cidade):
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def delete(self):
        banco.session.delete(self)
        banco.session.commit()
