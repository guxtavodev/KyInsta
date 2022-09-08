import pandas as pd

# carregar a base de dados

tabela = pd.read_excel("TrendsDiaria.xlsx")

# variaveis de classificação dos vídeos

videosMaiores = []

videosMedios = []

videosPequenos = []

# repetição para classificar os vídeos

linha=0

for linha in range(tabela.shape[0]):

	v = tabela.loc[linha, "Quantidade de vídeos"]	print(v)

	if v < 5000:

		videosPequenos.append(f'{tabela.loc[linha, "Hashtag"]}: {tabela.loc[linha, "Tema"]}')

	if v > 7000 and v < 7499:

		videosMedios.append(f'{tabela.loc[linha, "Hashtag"]}: {tabela.loc[linha, "Tema"]}')

	if v > 7500:

		videosMaiores.append(f'{tabela.loc[linha, "Hashtag"]}: {tabela.loc[linha, "Tema"]}')

	linha+1

print(videosPequenos)

print(videosMedios)

print(videosMaiores)

print(tabela)
