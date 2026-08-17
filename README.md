Mini-Projeto Avaliativo - Análise de Dados com Python T4
Aluno: Rutineia Avila  
Turma: Análise_de_Dados_T1  

Processos de ETL e Qualidade de Dados
O processo de ETL foi fundamental neste projeto. Ficou claro que dados brutos sempre vêm com problemas e não podem ser usados de imediato.
Extração: A leitura foi feita usando Pandas, onde o separador de ponto e vírgula impediu que as colunas fossem corrompidas.
Transformação: Tratar valores nulos (como definir "Sem Categoria" para produtos vazios ou assumir 0 para o número de filhos) evitou distorções nos calculos. Ajustar as datas de texto para o tipo datetime garantiu análises temporais cronologicamente corretas.

Principais Resultados
1. Público Alvo: O público Feminino (F) lidera o volume de consumo na plataforma, acumulando mais de 382 mil transações.
2. Dominância de Mercado: A categoria de ALIMENTOS é a campeã isolada de vendas com 384.197 itens vendidos, mostrando o forte apelo essencial da rede varejista.
3. Análise Demográfica: Embora a média indique que os clientes têm cerca de 1.15 filhos, a Moda e a Mediana cravadas em 0 provam que a grande maioria dos consumidores não possui filhos.
4. Qualidade da Amostra: O processo de limpeza foi essencial, removendo registros com IDs zerados e eliminando duplicatas geradas por falhas de integração do sistema de vendas.

Como Executar o Script
O script foi desenvolvido utilizando a biblioteca Pandas no ambiente Anaconda. Para rodar:
1. Certifique-se de ter o arquivo varejo.csv na mesma pasta do script.
2. Abra o arquivo Projeto_07.py no VS Code.
3. Altere o interpretador do Python para a versão do Conda (base 3.13.9).
4. Clique em executar.
