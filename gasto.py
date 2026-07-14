class Gasto:
    def __init__(self, categoria, nome, data, valor):
        self.__categoria = categoria
        self.__nome = nome
        self.__data = data
        self.__valor = valor

    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, nova_categoria):
        self.__categoria = nova_categoria

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, nova_data):
        self.__data = nova_data

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, novo_valor):
        self.__valor = novo_valor

    