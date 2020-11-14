

class Conta:

    def __init__(self, numero, titular, saldo, limite=0):
        print("Construindo objeto {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        return self.__saldo

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, conta_destino):
        self.saca(valor)
        conta_destino.deposita(valor)