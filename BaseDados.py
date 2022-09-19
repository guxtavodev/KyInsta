import pandas as pd
import openpyxl

class Excel:
	def ClassificarTrends():
	    videosMaiores=[]
	    videosMedios=[]
	    videosPequenos=[]
	    tabela = pd.read_excel("TrendsDiaria.xlsx")
	    numeroDeLinhas = tabela.dropna(how='all').shape[0]
	    linha=0
	    for linha in range(tabela.shape[0]):
	     rep = tabela.loc[linha, "Quantidade de vídeos"]
	     if rep < 600:
	     	videosPequenos.append(f"{tabela.loc[linha, 'Hashtag']}: {tabela.loc[linha, 'Tema']}")
	     if rep > 600 and rep < 1200:
	     	videosMedios.append(f"{tabela.loc[linha, 'Hashtag']}: {tabela.loc[linha, 'Tema']}")
	     if rep > 1201:
	     	videosMaiores.append(f"{tabela.loc[linha, 'Hashtag']}: {tabela.loc[linha, 'Tema']}")
	     linha+1
	    print("".join(map(str,videosMaiores)))
