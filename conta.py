class Conta:

    def __init__(self, numero, titular, saldo, limite=0):
        print("Construindo objeto {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo na conta de {0} é {1}".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor solicitado é maior do que o saldo disponível.")

    def __pode_sacar(self, valor):
        saldo_disponivel = self.__saldo + self.__limite
        return (valor <= saldo_disponivel)

    def transfere(self, valor, conta_destino):
        self.saca(valor)
        conta_destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def numero(self):
        return self.__numero

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}
