from gasto import Gasto
import dados

class Gerenciador:
    def __init__(self):
        self.__gastos = []

    
    def adicionar(self,categoria,nome,data,valor):
        novo_gasto = Gasto(categoria,nome,data,valor)

        self.__gastos.append(novo_gasto)

    def listar(self):
        return self.__gastos

    def remover(self, indice):
        if 0 <= indice < len(self.__gastos):
            self.__gastos.pop(indice)
            return True
        return False
    
    def editar(self, indice, nova_categoria, novo_nome, nova_data, novo_valor):
        if 0 <= indice < len(self.__gastos):
            gasto_editado = self.__gastos[indice]
            gasto_editado.categoria = nova_categoria
            gasto_editado.nome = novo_nome
            gasto_editado.data = nova_data
            gasto_editado.valor = novo_valor

            return True
        return False
        
    def total(self):
        soma_gastos = 0
        for gasto in self.__gastos:
            soma_gastos += gasto.valor

        return soma_gastos
    
    def filtrar_categoria(self, categoria_especifica):
        gastos_categoria = []

        for gasto in self.__gastos:
            if gasto.categoria == categoria_especifica:
                gastos_categoria.append(gasto)
            
        return gastos_categoria

    def total_categoria(self,categoria_escolhida):
        categoria_calcular_total = self.filtrar_categoria(categoria_escolhida)

        soma_categoria = 0

        for gasto in categoria_calcular_total:
            soma_categoria += gasto.valor

        return soma_categoria


    def relatorio_mensal(self, mes_escolhido, ano_escolhido):
        gasto_mes = []  
        gabarito_data = f"{mes_escolhido}/{ano_escolhido}"

        for gasto in self.__gastos:
            if str(gasto.data)[3:] == gabarito_data:
                gasto_mes.append(gasto)

        return gasto_mes
    
    def salvar_dados(self): #salva a lista gastos no formato excel
        dados.salvar(self.__gastos, "minhas_financas.xlsx")

    def carregar_dados(self): # carrega o formato excel de volta para a lista gastos
        try: #tenta ler o arquivo
            self.__gastos = dados.ler("minhas_financas.xlsx")
        
        except FileNotFoundError: #se o arquivo nao existir só ignora
            pass


