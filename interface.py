import sys
from gerenciador import Gerenciador
from PySide6.QtWidgets import QDialog, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QTabWidget, QHBoxLayout, QTableWidget, QTableWidgetItem
from PySide6.QtWidgets import QComboBox, QDoubleSpinBox, QDateEdit, QLabel, QTextEdit, QSpinBox
from PySide6.QtCore import QDate # Necessário para pegar a data de hoje


# Criação da Classe da Tela (Herdando da Janela Principal)
class TelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # Inicializa as configurações originais da janela
        self.setWindowTitle("Meu Gerenciador Financeiro")
        self.resize(600, 400) # Define a Largura x Altura inicial

        self.meu_gerenciador = Gerenciador()
        self.meu_gerenciador.carregar_dados()

        #cria um sistema de abas -> cada página é uma tela diferente
        self.sistema_abas = QTabWidget()
        self.setCentralWidget(self.sistema_abas)

        self.aba_cadastro() # primeira aba

        self.aba_consulta()

        self.aba_relatorio()

        self.atualizar_tabela() # Garante que a tabela nasça preenchida


    #Função visual -> faz apenas a parte visual
    def aba_cadastro(self):
        # Criando o Layout
        layout = QVBoxLayout()
        
        #Nome do gasto
        self.campo_nome = QLineEdit() # instanciando um objeto dessa classe -> criando uma caixa de texto
        self.campo_nome.setPlaceholderText("Digite o nome do gasto...") #Placeholder" é aquele texto cinza clarinho que fica dentro das caixas de formulário na internet e some sozinho quando você começa a digitar.
        
        #escolher a categoria
        self.campo_categoria = QComboBox() #cria aquela setinha que o usuário clica e escolhe uma opção
        self.campo_categoria.addItems(["Alimentação", "Transporte", "Educação","Lazer","Outros"])

        #valor
        self.campo_valor = QDoubleSpinBox() # cria uma caixinha que só aceita números decimais
        self.campo_valor.setMaximum(999999.99) # Define um limite máximo
        self.campo_valor.setPrefix("R$ ") # Coloca um "R$" visual na frente do número


        #Data
        self.campo_data = QDateEdit()
        self.campo_data.setCalendarPopup(True)# Faz abrir um mini calendário de verdade ao clicar
        self.campo_data.setDisplayFormat("dd/MM/yyyy") #formato da data
        self.campo_data.setDate(QDate.currentDate()) #Preenche com a data atual

        
        self.botao_salvar = QPushButton("Salvar Gasto") # classe que desenha um botao 3D clicável
        
        #Empilhando os widgets dentro do layout vertical
        # como o layout é vertical, o primeiro que entregamos fica no topo da tela, o segundo entra abaixo
        layout.addWidget(self.campo_nome) #Adicionar elemento visual -> pegando os objetos que estavam "invisíveis" na memória e entregando para o layout organizar na tela
        layout.addWidget(self.campo_categoria)
        layout.addWidget(self.campo_data)
        layout.addWidget(self.campo_valor)
        layout.addWidget(self.botao_salvar)

        #Criando um Widget para segurar o layout
        #Aqui você cria o piso (QWidget), prega toda a sua organização de móveis em cima desse piso (.setLayout(layout))
        piso_cadastro = QWidget()
        piso_cadastro.setLayout(layout)
        self.sistema_abas.addTab(piso_cadastro, "Cadastrar Novo Gasto") # insere como primeira aba do sistema_abas

        self.botao_salvar.clicked.connect(self.salvar_novo_gasto)


    #Função lógica -> instancia obj e salva
    def salvar_novo_gasto(self):
        # A coleta (Extrair os dados da tela) -> getters / suga o que o usuário digitou
        nome_digitado = self.campo_nome.text() #copia o que está no QLineEdit
        categoria_escolhida = self.campo_categoria.currentText() # Exclusivo do QComboBox -> vai na lista e vê qual palavra está aparecendo na tela
        valor_digitado = self.campo_valor.value() # Exclusivo do QDoubleSpinBox -> suga o float
        data_escolhida = self.campo_data.text() # Pega a data do calendário
       
        # A entrega -> instanciar o objeto
        self.meu_gerenciador.adicionar(categoria_escolhida,nome_digitado,data_escolhida,valor_digitado)

        # O salvamento
        self.meu_gerenciador.salvar_dados()

        # Apagamos o que o usuário escreveu na tela para ele poder cadastrar outro gasto
        self.campo_nome.clear() #apaga o que está no QLineEdit
        self.campo_valor.setValue(0.0) #força o campo do número voltar para zero

        self.atualizar_tabela() # Atualiza a aba de consulta com o novo gasto


    #constroi a parte visual da aba de consulta
    def aba_consulta(self):
        # Criando o Layout
        layout_principal = QVBoxLayout() # vertical -> empilha de cima para baixo

        layout_topo = QHBoxLayout() # horizontal -> lado a lado

        self.combo_filtro_categoria = QComboBox()
        self.combo_filtro_categoria.addItems(["Todas as Categorias", "Alimentação", "Transporte", "Educação", "Lazer", "Outros"])
        self.botao_filtrar = QPushButton("Filtrar")
        

        # Empilhamos o combo e o botão LADO A LADO no layout do topo
        layout_topo.addWidget(self.combo_filtro_categoria)
        layout_topo.addWidget(self.botao_filtrar)

        # Inserimos esse bloco horizontal dentro do layout principal vertical
        layout_principal.addLayout(layout_topo)

        # meio da tabela
        # criamos a tabela -> 4 colunas
        self.tabela_gastos = QTableWidget()
        self.tabela_gastos.setColumnCount(4)
        self.tabela_gastos.setHorizontalHeaderLabels(["Categoria", "Nome", "Data", "Valor"])
        self.tabela_gastos.horizontalHeader().setStretchLastSection(True) # Estica a última coluna
        
        #Cria o texto inicial
        self.label_total = QLabel("Total: R$ 0.00")
        
        #Deixar a letra maior e em negrito usando CSS)
        self.label_total.setStyleSheet("font-size: 16px; font-weight: bold; color: blue;")

        # A tabela vai sozinha no layout principal, ocupando o maior espaço
        layout_principal.addWidget(self.tabela_gastos)
        layout_principal.addWidget(self.label_total)

       
        layout_base = QHBoxLayout() # Horizontal
        
        self.botao_editar = QPushButton("Editar Selecionado")
        self.botao_remover = QPushButton("Remover Selecionado")
        
        # Os dois botões ficam lado a lado embaixo da tabela
        layout_base.addWidget(self.botao_editar)
        layout_base.addWidget(self.botao_remover)
        
        layout_principal.addLayout(layout_base)

       
        piso_consulta = QWidget()
        piso_consulta.setLayout(layout_principal)
        self.sistema_abas.addTab(piso_consulta, "Consulta de Gastos")


        self.botao_remover.clicked.connect(self.remover_selecionado)
        self.botao_editar.clicked.connect(self.editar_selecionado)
        self.botao_filtrar.clicked.connect(self.aplicar_filtro)
   

    def atualizar_tabela(self):
        self.tabela_gastos.setRowCount(0) # sempre que for  atualizar limpamos o que estava lá na tabela antes

        lista = self.meu_gerenciador.listar() #pega a lista atualizada

        for gasto in lista:
            
            # Pergunta para a tabela qual é a próxima linha vazia no final dela
            linha_atual = self.tabela_gastos.rowCount()

            # Insere uma linha em branco exatamente nessa coordenada
            self.tabela_gastos.insertRow(linha_atual)

            #Ela exige que todo dado seja empacotado em um "recipiente visual" (QTableWidgetItem)
            gasto_categoria = QTableWidgetItem(str(gasto.categoria))
            gasto_nome = QTableWidgetItem(str(gasto.nome))
            gasto_data = QTableWidgetItem(str(gasto.data))

            #transformar o float em texto formatado
            texto_formatado = f"R$ {gasto.valor:.2f}"
            gasto_valor = QTableWidgetItem(texto_formatado)

            # Posiciona nas colunas daquela nova linha
            self.tabela_gastos.setItem(linha_atual,0,gasto_categoria)
            self.tabela_gastos.setItem(linha_atual,1,gasto_nome)
            self.tabela_gastos.setItem(linha_atual,2,gasto_data)
            self.tabela_gastos.setItem(linha_atual,3,gasto_valor)

        soma_total = self.meu_gerenciador.total()

        texto_final = f"Total: R$ {soma_total:.2f}"
        self.label_total.setText(texto_final)   
    def remover_selecionado(self):
        # retorna o indice onde o usuário clicou por ultimo
        gasto_selecionado = self.tabela_gastos.currentRow() # retorna o número exato da linha que está selecionada

        if gasto_selecionado >= 0:
            self.meu_gerenciador.remover(gasto_selecionado)

            self.atualizar_tabela()

    def aplicar_filtro(self):
        #Sugamos a palavra que o usuário deixou selecionada na caixinha
        categoria_escolhida = self.combo_filtro_categoria.currentText()

        #Limpamos a tabela velha
        self.tabela_gastos.setRowCount(0)

        if categoria_escolhida == "Todas as Categorias":
            lista = self.meu_gerenciador.listar()
            soma_total = self.meu_gerenciador.total() # Usa a função que você já tinha!
        else:
            lista = self.meu_gerenciador.filtrar_categoria(categoria_escolhida)
            soma_total = self.meu_gerenciador.total_categoria(categoria_escolhida)
        
        for gasto in lista:
            linha_atual = self.tabela_gastos.rowCount() #saber quantas linhas tem na tabela atualmente
            self.tabela_gastos.insertRow(linha_atual) #constroi uma linha em branco na posição

            #preenchendo a linha em branco
            self.tabela_gastos.setItem(linha_atual, 0, QTableWidgetItem(str(gasto.categoria)))
            self.tabela_gastos.setItem(linha_atual, 1, QTableWidgetItem(str(gasto.nome)))
            self.tabela_gastos.setItem(linha_atual, 2, QTableWidgetItem(str(gasto.data)))
            self.tabela_gastos.setItem(linha_atual, 3, QTableWidgetItem(f"R$ {gasto.valor:.2f}"))

        self.label_total.setText(f"Total: R$ {soma_total:.2f}")  


    def editar_selecionado(self):
        #descobre qual linha o usuário clicou na tabela
        linha_atual = self.tabela_gastos.currentRow()

        #verifica se ele realmente selecionou algo
        if linha_atual>= 0:
            #pega a lista
            lista = self.meu_gerenciador.listar()
            gasto_antigo = lista[linha_atual]

            #instancia a janela passando o gasto antigo
            janela = JanelaEdicao(gasto_antigo)

            #O .exec() abre a janela e trava o código aqui.
            #Usuário pode editar agora
            if janela.exec() == QDialog.Accepted:

                #O usuário confirmou! Agora sugamos os dados novos que ele digitou 
                novo_nome = janela.campo_nome.text()
                nova_categoria = janela.campo_categoria.currentText()
                novo_valor = janela.campo_valor.value()
                nova_data = janela.campo_data.text()


                #Mandamos a função substituir os dados antigos pelos novos
                self.meu_gerenciador.editar(linha_atual, nova_categoria, novo_nome, nova_data, novo_valor)


                #Salvamos no arquivo JSON/Excel e redesenhamos a tabela
                self.meu_gerenciador.salvar_dados()
                self.atualizar_tabela()

    
    def aba_relatorio(self):
        layout_principal = QVBoxLayout()
        piso_relatorio = QWidget()

        #Criando a área de filtros (Mês e Ano)
        layout_filtros = QHBoxLayout()

        self.combo_mes = QComboBox()
        self.combo_mes.addItems(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"])


        self.campo_ano = QSpinBox()
        self.campo_ano.setRange(2000, 2100) # Limites de ano
        self.campo_ano.setValue(2026) # Ano inicial padrão


        self.botao_gerar = QPushButton("Gerar Relatório")

        # Empilhando os filtros lado a lado (com Textos explicativos)
        layout_filtros.addWidget(QLabel("Mês:"))
        layout_filtros.addWidget(self.combo_mes)
        layout_filtros.addWidget(QLabel("Ano:"))
        layout_filtros.addWidget(self.campo_ano)
        layout_filtros.addWidget(self.botao_gerar)

        #Criando o "Bloco de Notas" onde o texto vai aparecer
        self.area_relatorio = QTextEdit()
        # Impedimos o usuário de apagar o texto do relatório sem querer:
        self.area_relatorio.setReadOnly(True)

        #Juntando tudo no layout principal
        layout_principal.addLayout(layout_filtros)
        layout_principal.addWidget(self.area_relatorio)


        piso_relatorio.setLayout(layout_principal)
        self.sistema_abas.addTab(piso_relatorio, "Relatório Mensal")


        self.botao_gerar.clicked.connect(self.gerar_relatorio)



    def gerar_relatorio(self):
    
        mes_escolhido = self.combo_mes.currentText()
        ano_escolhido = str(self.campo_ano.value())

        lista_do_mes = self.meu_gerenciador.relatorio_mensal(mes_escolhido, ano_escolhido)

        total_mensal = 0.0
        gastos_por_categoria = {"Alimentação": 0.0, "Transporte": 0.0, "Educação": 0.0, "Lazer": 0.0, "Outros": 0.0}

        for gasto in lista_do_mes:
            valor = float(gasto.valor)
            total_mensal += valor
            
            if gasto.categoria in gastos_por_categoria:
                gastos_por_categoria[gasto.categoria] += valor

        #(Construindo o texto formatado)
        texto_final = f"=== RELATÓRIO MENSAL ({mes_escolhido}/{ano_escolhido}) ===\n\n"
        texto_final += f"TOTAL GASTO NO MÊS: R$ {total_mensal:.2f}\n"
        texto_final += "--------------------------------------\n"
        texto_final += "DETALHAMENTO POR CATEGORIA:\n\n"

        for categoria, valor in gastos_por_categoria.items():
            if valor > 0: # Só imprime se o usuário tiver gasto algo naquela categoria
                texto_final += f" 🔹 {categoria}: R$ {valor:.2f}\n"
        
        if total_mensal == 0:
            texto_final += "\nNenhum gasto registrado neste mês. Parabéns pela economia!"

        # 6. O Setter! Esmagamos esse texto gigante dentro da nossa pecinha de bloco de notas
        self.area_relatorio.setText(texto_final)
        
class JanelaEdicao(QDialog): # QDualog já é um QWidget por natureza -> não precisa criar um
    def __init__(self, gasto_antigo):
        super().__init__()
        self.setWindowTitle("Editar Gasto")


        #layout da janelinha
        Layout = QVBoxLayout()

        #criamos os campos (igual na aba cadastro)
        self.campo_nome = QLineEdit() #criamos a caixinha do input vazia
        self.campo_categoria = QComboBox()
        self.campo_categoria.addItems(["Alimentação", "Transporte", "Educação", "Lazer", "Outros"])
        self.campo_valor = QDoubleSpinBox()
        self.campo_valor.setMaximum(999999.99)
        self.campo_data = QDateEdit()
        self.campo_data.setCalendarPopup(True)# Faz abrir um mini calendário de verdade ao clicar
        self.campo_data.setDisplayFormat("dd/MM/yyyy") #formato da data
        self.campo_data.setDate(QDate.currentDate()) #Preenche com a data atual


        #Prenchendo os campos com os dados do gasto_antigo
        self.campo_nome.setText(gasto_antigo.nome)
        self.campo_categoria.setCurrentText(gasto_antigo.categoria)
        self.campo_valor.setValue(float(gasto_antigo.valor))
        #Essa linha pega o texto, usa o gabarito "dd/MM/yyyy" para entender a ordem dos números, e transforma isso em um Objeto de Data do Python.
        data_string_convertida = QDate.fromString(gasto_antigo.data,"dd/MM/yyyy")
        #Essa linha pega o calendário visual da tela e diz: "Mude a sua exibição visual e pule lá para essa data aqui"
        self.campo_data.setDate(data_string_convertida)


        # Criamos o botão de confirmar a edição
        self.botao_salvar = QPushButton("Atualizar")

        # Empilhamos tudo no layout da janelinha
        Layout.addWidget(self.campo_nome)
        Layout.addWidget(self.campo_categoria)
        Layout.addWidget(self.campo_valor)
        Layout.addWidget(self.campo_data)
        Layout.addWidget(self.botao_salvar)

        self.setLayout(Layout)

        # Se o usuário clicar em "Atualizar", a janelinha fecha e avisa que deu tudo certo!
        self.botao_salvar.clicked.connect(self.accept)
        




        

