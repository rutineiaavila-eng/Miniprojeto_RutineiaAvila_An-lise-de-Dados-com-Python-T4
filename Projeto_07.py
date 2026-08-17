# Projeto de Analise de Dados - Modulo 1 / Semana 7
# Aluno: [Seu Nome Completo]
# Turma: Analise_de_Dados_T1
import os
import pandas as pd

arquivo_alvo = 'varejo.csv'
pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(pasta_atual, arquivo_alvo)

# Carrega a base com o separador correto pra nao quebrar as colunas
df = pd.read_csv(caminho_csv, sep=';')

# --- ETAPA 2 e 3: Limpeza dos dados ---

# 1. Filtra IDs invalidos (tira zeros e nulos)
df['CO_ID'] = df['CO_ID'].astype(str).str.strip()
df = df[(df['CO_ID'] != '') & (df['CO_ID'] != '0') & (df['CO_ID'] != 'nan')]

# 2. Apaga as linhas repetidas
df = df.drop_duplicates()

# 3. Coloca texto nas categorias que vieram vazias
df['PR_CAT'] = df['PR_CAT'].fillna('Sem Categoria')
df.loc[df['PR_CAT'].str.strip() == '', 'PR_CAT'] = 'Sem Categoria'

# 4. Se o numero de filhos ta vazio, vira 0
df['CL_FHL'] = df['CL_FHL'].fillna(0).astype(int)

# 5. Muda o texto da data para tipo data de verdade
df['DATA'] = pd.to_datetime(df['DATA'], errors='coerce')


print("--- ETAPA 4: Contas Estatisticas (Coluna Filhos) ---")

# Fazendo as metricas obrigatorias de filhos de forma direta
contagem = df['CL_FHL'].count()
media = df['CL_FHL'].mean()
mediana = df['CL_FHL'].median()
moda = int(df['CL_FHL'].mode()[0])
minimo = df['CL_FHL'].min()
maximo = df['CL_FHL'].max()
desvio_padrao = df['CL_FHL'].std()
q1 = df['CL_FHL'].quantile(0.25)
q3 = df['CL_FHL'].quantile(0.75)

print(f"Quantidade total: {contagem}")
print(f"Media de filhos: {media:.2f}")
print(f"Mediana de filhos: {mediana}")
print(f"Moda de filhos: {moda}")
print(f"Minimo: {minimo} | Maximo: {maximo}")
print(f"Desvio Padrao: {desvio_padrao:.2f}")
print(f"Quartil 1 (25%): {q1}")
print(f"Quartil 3 (75%): {q3}\n")


print("--- ETAPA 5: Agrupamentos e Resultados Finais ---")

# Agrupamento 1: Vendas por Genero usando o groupby do pandas
agrupado_genero = df.groupby('CL_GENERO').size()
print("Distribuição por Gênero:")
for genero, qtd in agrupado_genero.items():
    print(f" - {genero}: {qtd} compras")

# Agrupamento 2: Vendas por Categoria ordenado do maior pro menor
agrupado_cat = df.groupby('PR_CAT').size().sort_values(ascending=False)
print("\nDistribuição por Categoria (Ordenado por Volume):")
for categoria, qtd in agrupado_cat.items():
    print(f" - {categoria}: {qtd} itens")
