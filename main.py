# imports

from flask import Flask, render_template, jsonify, request
import pandas as pd
import openpyxl
import BaseDados
import random
from ins import *

print(Relatorio(50, 50, 50))

# Importando Modulo do Excel
Excel = BaseDados.Excel

Excel.ClassificarTrends()

# Bloco das classificações de vídeos
videosMaiores=[]
videosMedios=[]
videosPequenos=[]

# carrega os dados
tabela = pd.read_excel("TrendsDiaria.xlsx")
numeroDeLinhas = tabela.dropna(how='all').shape[0]
# Aqui ja vai escrevendo os videos de acordo com a classificação 
linha=0
for linha in range(tabela.shape[0]):
	     rep = tabela.loc[linha, "Quantidade de vídeos"]
	     if rep < 600:
	     	videosPequenos.append(f"{tabela.loc[linha, 'Hashtag']}: {tabela.loc[linha, 'Tema']}")
	     if rep > 600 and rep < 1200:
	     	videosMedios.append(f"{tabela.loc[linha, 'Hashtag']}: {tabela.loc[linha, 'Tema']}")
	     if rep > 1201:
	     	videosMaiores.append(f"<p id='tab'>{tabela.loc[linha, 'Hashtag']}: {tabela.loc[linha, 'Tema']}</p><br>")
	     linha+1

# Bloco das legendas recomendadas

legendas = [
	"<p id='tab'>Eu sou o melhor de mim!</p><br>",
	"<p id='tab'>Deixando a vida fluir. Pode levar o que não é para ficar e trazer o que me fará bem.</p><br>",
	"<p id='tab'>Em (re)construção. Ainda bem.</p>"
]

# Já vai inicializando o site.
app = Flask(__name__)

def gerarToken():
	inicio = [
		"hd",
		"ys",
		"hh",
		"hi",
		"jd",
		"jx"
	]
	meio = [
		"in",
		"tk",
		"ki",
		"ij",
		"js",
		"dj"
	]
	final = [
		"hx",
		"mx",
		"jf",
		"cj",
		"cc",
		"jx"
	]
	tokenFinal = random.choice(inicio) + random.choice(meio) + random.choice(final)
	return tokenFinal


# Página Inicial
@app.route("/", methods=["GET", "POST"])
def homepage():
	#	sg = request.form["followers"]
	#	ts = request.form["contasa"]
	#	js = request.form["en"]
	fl = int(request.args.get("followers"))
	ca = int(request.args.get("contasa"))
	en = int(request.args.get("en"))
	usj = Relatorio(en, ca, fl)
		
	return render_template('index.html', videos="".join(map(str,videosMaiores)), legendasr="".join(map(str,legendas)), uis="".join(map(str, usj)))

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
	if request.method == "POST":
		username = request.form["username"]
		plataforma = request.form["plt"]
		print("====> Novo usuário!")
		print("Username: ", username)
		print("Plataforma: ", plataforma)
	return render_template("signup.html")
	
@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "POST":
		token = request.form["token"]
	
	return render_template("sign-in.html")
	

# Dar run webapp
if __name__ == "__main__":
	app.run(host="0.0.0.0")
