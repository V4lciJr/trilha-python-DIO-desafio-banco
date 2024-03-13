class Endereco:

    def __init__(self, logradouro, numero_casa, bairro, cidade, estado):
        self.__logradouro = logradouro
        self.__numero_casa = numero_casa
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado

    @property
    def logradouro(self):
        return self.__logradouro

    @property
    def numero_casa(self):
        return self.__numero_casa

    @property
    def bairro(self):
        return self.__bairro

    @property
    def cidade(self):
        return self.__cidade

    @property
    def estado(self):
        return self.__estado

    def __str__(self):
        return f"""Rua: {self.logradouro}, {self.numero_casa}. Bairro: {self.bairro}
                   {self.cidade} - {self.estado}"""
