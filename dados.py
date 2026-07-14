from gasto import Gasto
import pandas as pd

def salvar(lista, caminho_arquivo):
    lista_de_dicionarios = []

    for gasto in lista:
        #cria um dicionario com as propriedades de cada obj e adiciona na lista
        novo_gasto = {'gasto':gasto.nome, 'categoria': gasto.categoria, 'data': gasto.data,'valor': gasto.valor}
        lista_de_dicionarios.append(novo_gasto)

    #transforma a lista de dicionarios em uma "matriz" ->dataframe
    df = pd.DataFrame(lista_de_dicionarios)
    df.to_excel(caminho_arquivo,index = False) 


def ler(caminho_arquivo):
    #carrega a planilha para a memória
    df = pd.read_excel(caminho_arquivo)
    #transformar esse dataframe de volta em uma lista de dicionários
    lista_dicionarios = df.to_dict('records') #records avisa o pandas para transformar cada linha da planilha em um dicionário

    #agora tem uma lista de dicionários -> porém o gerenciador só trabalha com objetos Gasto
    #transformar os dicionários em objetos Gastos
    lista_pronta = []

    for linha in lista_dicionarios:
        novo_obj = Gasto(linha['categoria'],linha['gasto'], linha['data'],linha['valor'])
        lista_pronta.append(novo_obj)

    return lista_pronta

