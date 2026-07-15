# 📊 Gerenciador Financeiro Pessoal

Um sistema completo de gestão financeira com interface gráfica interativa e um painel analítico (Dashboard) integrado. Desenvolvido para facilitar o controle de gastos diários, permitindo o cadastro de despesas e a visualização de métricas de consumo de forma clara e executiva.

## 💡 Ideia do Projeto

O objetivo deste projeto é criar uma solução de ponta a ponta para o controle de finanças pessoais. Em vez de depender de planilhas manuais complexas, o usuário interage com um software Desktop amigável para registrar os gastos, enquanto um Dashboard profissional em Power BI consome esses dados para gerar insights automáticos, separando perfeitamente a camada de aplicação da camada de análise de dados.

## ✨ Funcionalidades

* **Cadastro de Despesas:** Inserção rápida de novos gastos com valor, data e categoria.
* **Categorização Inteligente:** Divisão dos gastos em categorias (Alimentação, Lazer, Educação, Transporte, Outros).
* **Persistência de Dados Local:** Salvamento automático das informações em uma base de dados local (Excel), garantindo privacidade total (os dados do usuário não sobem para a nuvem).
* **Interface Gráfica (GUI):** Telas modernas e intuitivas desenvolvidas com PySide6.
* **Dashboard Executivo:** Painel em Power BI para acompanhamento de totais, médias, gráfico de rosca (distribuição por categoria) e gráfico de colunas (evolução diária).

## 🛠️ Tecnologias Utilizadas

* **Back-end & Lógica:** Python
* **Interface Gráfica (GUI):** PySide6
* **Armazenamento de Dados:** Planilha Excel (`.xlsx`)
* **Análise de Dados (BI):** Microsoft Power BI
* **Versionamento:** Git & GitHub

---

## 🚀 Como Rodar o Projeto (Aplicação Python)

### Pré-requisitos

* Ter o [Python](https://www.python.org/downloads/) instalado na sua máquina.
* (Recomendado) Criar um ambiente virtual.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/AnaBeatrizGuimaraes/gerenciador-financeiro-python.git](https://github.com/AnaBeatrizGuimaraes/gerenciador-financeiro-python.git)
