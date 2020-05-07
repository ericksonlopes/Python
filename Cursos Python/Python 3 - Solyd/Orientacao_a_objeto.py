class Cliente:
    def __init__(self, nome, cpf, idade):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade

    def dados_cliente(self):
        return {'nome': self.__nome,
                'cpf': self.__cpf,
                'idade': self.__idade}


class Conta(Cliente):
    def __init__(self, nome, cpf, idade, saldo, limite):
        super().__init__(nome, cpf, idade)
        # Representante da conta
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade

        # dados da conta
        self.__saldo = float(saldo)
        self.__limite = float(limite)

    def saldo_atual(self):
        print(f'Saldo atual: R${self.__saldo:.2f}')

    def dono(self):
        print('nome: ', self.__nome)
        print('cpf:', self.__cpf)
        print('idade :', self.__idade)

    def sacar(self, valor_saque):
        self.__saldo -= float(valor_saque)
        print(f'Saque de R${valor_saque}, Realizado com sucesso!')

    def depositar(self, valor_deposito):
        self.__saldo += float(valor_deposito)


cliente = Cliente('Erickson', '19542634-05', 18)

dc = cliente.dados_cliente()

conta = Conta(dc['nome'], dc['cpf'], dc['idade'], 1500.00, 5000.00)

conta.saldo_atual()
conta.sacar(257.05)
conta.saldo_atual()

conta.saldo_atual()
conta.depositar(750.00)
conta.saldo_atual()


