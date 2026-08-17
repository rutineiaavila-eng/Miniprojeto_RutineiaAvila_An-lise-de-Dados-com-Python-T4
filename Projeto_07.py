# projeto de analise de dados - modulo 1 / semana 7
# aluna: Rutineia Avila
# turma: Analise_de_Dados_T1

import os
import pandas as pd

arquivo = 'varejo.csv'
pasta_local = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(pasta_local, arquivo)

df = pd.read_csv(caminho_csv, sep=';')

# --- comeco da limpeza da base ---
df['CO_ID'] = df['CO_ID'].astype(str).str.strip()
df = df[(df['CO_ID'] != '') & (df['CO_ID'] != '0') & (df['CO_ID'] != 'nan')]

df = df.drop_duplicates()

df['PR_CAT'] = df['PR_CAT'].fillna('Sem Categoria')
df.loc[df['PR_CAT'].str.strip() == '', 'PR_CAT'] = 'Sem Categoria'

df['CL_FHL'] = df['CL_FHL'].fillna(0).astype(int)
df['DATA'] = pd.to_datetime(df['DATA'], errors='coerce')

# --- calculos estatisticos de filhos ---
print("--- METRICAS DA COLUNA FILHOS ---")
linhas_limpas = df['CL_FHL'].count()
media_f = df['CL_FHL'].mean()
mediana_f = df['CL_FHL'].median()
moda_f = int(df['CL_FHL'].mode())
minimo_f = df['CL_FHL'].min()
maximo_f = df['CL_FHL'].max()
desvio_padrao_f = df['CL_FHL'].std()
q1 = df['CL_FHL'].quantile(0.25)
q3 = df['CL_FHL'].quantile(0.75)

print(f"Total de registros: {linhas_limpas}")
print(f"Media de filhos: {media_f:.2f}")
print(f"Mediana: {mediana_f}")
print(f"Moda: {moda_f}")
print(f"Minimo: {minimo_f} | Maximo: {maximo_f}")
print(f"Desvio Padrao: {desvio_padrao_f:.2f}")
print(f"Quartil 1 (25%): {q1}")
print(f"Quartil 3 (75%): {q3}\n")

# --- agrupamento dos resultados ---
print("--- QUANTIDADE DE COMPRAS POR GENERO ---")
tot_genero = df.groupby('CL_GENERO').size()
for genero, tot_vendas in tot_genero.items():
    print(f"Gênero {genero}: {tot_vendas} compras")
print("\n")

print("--- VENDAS POR CATEGORIA (ORDENADO) ---")
tot_categoria = df.groupby('PR_CAT').size().sort_values(ascending=False)
for categoria, tot_vendas in tot_categoria.items():
    print(f"{categoria}: {tot_vendas} itens")

# --- exportando o df_limpo exigido na sprint 6 ---
caminho_saida = os.path.join(pasta_local, 'varejo_limpo.csv')
df.to_csv(caminho_saida, sep=';', index=False)
print("\nArquivo criado com sucesso: varejo_limpo.csv")
