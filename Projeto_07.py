# Projeto de Analise de Dados - Modulo 1 / Semana 7
# Aluno: [Rutineia Cordeiro de Avila]
# Turma: Analise_de_Dados_T1

import os
import csv
from datetime import datetime

arquivo_alvo = 'varejo.csv'
pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(pasta_atual, arquivo_alvo)

linhas_brutas = []

with open(caminho_csv, mode='r', encoding='utf-8') as f:
    leitor = csv.DictReader(f, delimiter=';')
    for linha in leitor:
        linhas_brutas.append(dict(linha))

dados_limpos = []
erros_id = 0
erros_duplicados = 0
nulos_categoria = 0
linhas_vistas = set()

for registro in linhas_brutas:
    id_compra = registro.get('CO_ID', '').strip()
    if id_compra == '' or id_compra == '0':
        erros_id += 1
        continue

    conteudo_linha = tuple(registro.items())
    if conteudo_linha in linhas_vistas:
        erros_duplicados += 1
        continue
    linhas_vistas.add(conteudo_linha)

    categoria = registro.get('PR_CAT', '').strip()
    if categoria == '':
        nulos_categoria += 1
        registro['PR_CAT'] = "Sem Categoria"

    if registro.get('CL_FHL') == '' or registro.get('CL_FHL') is None:
        registro['CL_FHL'] = '0'

    txt_data = registro.get('DATA', '').strip()
    try:
        registro['DATA'] = datetime.strptime(txt_data, '%Y-%m-%d')
    except ValueError:
        try:
            registro['DATA'] = datetime.strptime(txt_data, '%d/%m/%Y')
        except ValueError:
            registro['DATA'] = None

    dados_limpos.append(registro)

print("--- ETAPA 2 e 3: Limpeza e Ajustes dos Dados ---")
print(f"-> Linhas descartadas por ID ruim: {erros_id}")
print(f"-> Linhas repetidas deletadas: {erros_duplicados}")
print(f"-> Categorias vazias corrigidas: {nulos_categoria}")
print(f"Total de registros limpos: {len(dados_limpos)}\n")

print("--- ETAPA 4: Calculos Estatisticos (Coluna Filhos) ---")
lista_filhos = []
for r in dados_limpos:
    if r['CL_FHL'] is not None:
        lista_filhos.append(int(r['CL_FHL']))

lista_filhos.sort()
total_linhas = len(lista_filhos)

soma_filhos = sum(lista_filhos)
media = soma_filhos / total_linhas

minimo = lista_filhos[0]
maximo = lista_filhos[-1]

if total_linhas % 2 == 1:
    mediana = lista_filhos[total_linhas // 2]
else:
    metade = total_linhas // 2
    mediana = (lista_filhos[metade - 1] + lista_filhos[metade]) / 2.0
    
contagem_votos = {}
for valor in lista_filhos:
    contagem_votos[valor] = contagem_votos.get(valor, 0) + 1

maior_ocorrencia = max(contagem_votos.values())
lista_modas = [chave for chave, qtd in contagem_votos.items() if qtd == maior_ocorrencia]
moda = lista_modas
    
soma_quadrados = 0
for valor in lista_filhos:
    soma_quadrados += (valor - media) ** 2

variancia = soma_quadrados / (total_linhas - 1)
desvio_padrao = variancia ** 0.5

idx_q1 = int(total_linhas * 0.25)
idx_q3 = int(total_linhas * 0.75)
q1 = lista_filhos[idx_q1]
q3 = lista_filhos[idx_q3]

print(f"Quantidade total: {total_linhas}")
print(f"Media de filhos: {media:.2f}")
print(f"Mediana de filhos: {mediana}")
print(f"Moda de filhos: {moda}")
print(f"Minimo: {minimo} | Maximo: {maximo}")
print(f"Desvio Padrao: {desvio_padrao:.2f}")
print(f"Quartil 1 (25%): {q1}")
print(f"Quartil 3 (75%): {q3}\n")

print("--- ETAPA 5: Agrupamentos e Resultados Finais ---")
contar_genero = {}
for r in dados_limpos:
    g = r.get('CL_GENERO', '').strip()
    if g == '':
        g = 'Nao Informado'
    contar_genero[g] = contar_genero.get(g, 0) + 1

print("Distribuição por Gênero:")
for genero, qtd in contar_genero.items():
    print(f" - {genero}: {qtd} compras")

contar_categoria = {}
for r in dados_limpos:
    cat = r.get('PR_CAT', 'Sem Categoria')
    contar_categoria[cat] = contar_categoria.get(cat, 0) + 1

print("\nDistribuição por Categoria (Ordenado por Volume):")
for categoria, qtd in sorted(contar_categoria.items(), key=lambda item: item[1], reverse=True):
    print(f" - {categoria}: {qtd} itens")
