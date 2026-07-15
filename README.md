# 📊 Gerenciador Financeiro Pessoal

Um sistema Desktop robusto para gestão de finanças pessoais, projetado para oferecer controle total sobre suas despesas diárias e mensais. O projeto une uma interface gráfica intuitiva para a operação do dia a dia com um Dashboard analítico avançado para a extração de insights financeiros, separando perfeitamente a aplicação da análise de dados.

## 💡 Utilidade e Ideia do Projeto

O foco principal deste sistema é substituir planilhas manuais e confusas por uma ferramenta onde o usuário possa registrar, gerenciar e analisar seu dinheiro de forma estruturada. Ele foi pensado para quem precisa de respostas rápidas sobre sua saúde financeira: "Para onde está indo meu dinheiro?", "Qual mês eu gastei mais?" e "Qual a minha média diária de gastos?". 

## 🖼️ Visão Geral do Dashboard
*(Abaixo está a interface analítica gerada a partir dos dados do sistema)*

![Dashboard Financeiro](images/dashboardd.png)
## ✨ Funcionalidades Principais

O sistema foi construído para cobrir todo o ciclo de vida de uma despesa, desde o cadastro até a análise visual:

* **Gestão Completa de Gastos (CRUD):** 
  * **Adicionar:** Inserção de novas despesas com valor, data, descrição e categoria.
  * **Listar:** Visualização de todos os gastos registrados em uma tabela limpa e organizada.
  * **Editar:** Correção rápida de valores ou categorias de despesas já cadastradas.
  * **Remover:** Exclusão de registros incorretos ou duplicados com facilidade.
* **Relatórios Mensais:** Filtragem e compilação automática dos gastos, permitindo que o usuário visualize exatamente o acumulado de um mês específico.
* **Categorização Inteligente:** Organização das despesas por áreas da vida (Alimentação, Lazer, Educação, Transporte, Outros) para identificar os maiores ralos financeiros.
* **Privacidade e Persistência Local:** Todo o banco de dados é gerado e salvo localmente no computador do usuário em formato Excel (`.xlsx`), garantindo que nenhuma informação financeira sensível seja enviada para a nuvem.

## 📈 O Dashboard Executivo (Power BI)

Para complementar o software, o projeto conta com um painel interativo construído em Power BI que consome os dados gerados pela aplicação e oferece uma visão gerencial:

* **Cartões de KPI (Indicadores Chave):** Exibição imediata do *Total Gasto no Mês*, valor da *Maior Compra* realizada e o *Gasto Médio* por despesa.
* **Distribuição por Categoria:** Um gráfico de rosca detalhado que mostra a porcentagem exata da sua renda direcionada para cada área (ex: 30% em Alimentação, 15% em Lazer).
* **Evolução Diária:** Um gráfico de colunas cronológico que mapeia o comportamento de consumo dia após dia, permitindo identificar picos de gastos ao longo do mês.
* **Extrato Detalhado:** Uma matriz/tabela inferior para consulta rápida de cada transação sem precisar abrir a aplicação principal.

## 🛠️ Tecnologias Utilizadas

* **Linguagem Principal:** Python (Back-end e Lógica de Negócios)
* **Interface Gráfica (GUI):** PySide6 (Framework Qt para Python)
* **Manipulação de Dados:** Bibliotecas Python para integração e geração de planilhas (`pandas` / `openpyxl`)
* **Armazenamento:** Planilha Excel (`.xlsx`)
* **Business Intelligence (BI):** Microsoft Power BI
* **Versionamento:** Git e GitHub

---

## 🚀 Como Rodar o Projeto Passo a Passo

### 1. Rodando o Programa Principal (Python)

**Pré-requisitos:**
* Ter o [Python](https://www.python.org/downloads/) instalado no computador.

**Passo a Passo:**
1. Abra o terminal (ou Prompt de Comando/PowerShell) na pasta onde deseja salvar o projeto.
2. Clone este repositório executando:

```bash
git clone https://github.com/AnaBeatrizGuimaraes/gerenciador-financeiro-python.git
```
3. Entre na pasta do projeto

```bash
cd gerenciador-financeiro-python
```

### Instale as dependências necessárias

Execute o comando abaixo para instalar as bibliotecas necessárias para a interface gráfica:

```bash
pip install PySide6 openpyxl pandas
```

> **Observação:** Se houver um arquivo `requirements.txt` no projeto, utilize o comando abaixo em vez do anterior:
>
> ```bash
> pip install -r requirements.txt
> ```

### Inicie a aplicação

```bash
python main.py
```

> **Nota:** Ao executar o programa pela primeira vez e cadastrar sua primeira despesa, o sistema criará automaticamente o arquivo do banco de dados `minhas_financas.xlsx` no seu computador.

---

### 2. Rodando e Conectando o Dashboard (Power BI)

O arquivo do Power BI disponível neste repositório contém **dados de demonstração** para que você possa visualizar o layout. Para conectá-lo aos seus próprios gastos gerados pela aplicação Python, siga os passos abaixo.

## Pré-requisitos

- Ter o **Power BI Desktop** instalado.
- Ter executado a aplicação Python e cadastrado pelo menos uma despesa (para gerar a planilha `minhas_financas.xlsx`).

## Passo a passo

1. Abra a pasta `dashboard` presente no repositório clonado.
2. Dê um duplo clique no arquivo `Dashboard_gestao_financeira.pbix` para abri-lo no Power BI.
3. No menu superior (**Página Inicial**), clique na seta ao lado do botão **Transformar Dados** e selecione **Configurações de fonte de dados**.
4. Na janela que será aberta, selecione o caminho do arquivo listado e clique em **Alterar Fonte...**.
5. Clique em **Procurar...** e navegue até a pasta raiz do projeto no seu computador.
6. Selecione o arquivo `minhas_financas.xlsx` gerado pela aplicação Python.
7. Clique em **OK** e feche a janela de configurações.
8. Por fim, clique no botão **Atualizar** (ícone de setas circulares) localizado na guia **Página Inicial**.

## Resultado

Após a atualização, os dados de demonstração serão substituídos automaticamente pelas informações reais cadastradas na aplicação Python. O dashboard passará a exibir e analisar todas as suas despesas registradas.
   
