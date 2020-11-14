
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print("{0:02}/{1:02}/{2:04}".format(self.dia, self.mes, self.ano))