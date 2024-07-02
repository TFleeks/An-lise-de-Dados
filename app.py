import pandas as pd
import plotly.express as px

# Passo 1 - Importar a base de dados

tabela = pd.read_csv("telecom_users.csv")

# Passo 2 - Visualizar a base de dados



# Passo 3 - Tratar os dados

tabela = tabela.drop("Unnamed: 0", axis=1)
tabela ["TotalGasto"] = pd.to_numeric(tabela ["TotalGasto"], errors="coerce")

# Tratamento de valores vazios

tabela = tabela.dropna(how="all", axis=1)
tabela = tabela.dropna(how="any", axis=0)

# Passo 4 - Analise inicial
print(tabela["Churn"].value_counts())

# Passo 5 - Analise detalhada dos clientes

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    grafico.show()