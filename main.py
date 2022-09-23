# imports

from flask import Flask, render_template, jsonify, request
import pandas as pd
import openpyxl
import random
from ins import *
import sqlite3
from flask_cors import CORS
import Db

db = Db.DB

conn = sqlite3.connect('tclientes.db') # definindo um cursor 
cursor = conn.cursor() # criando a tabela (schema)


# cursor.execute(""" 
#	INSERT INTO usr (username, token, plt)
# 	VALUES (?,?,?)
# """, ("GustavinNeh", "kkkk", "Instagram"))
# conn.commit()

def localizar_cliente(id):
	r = cursor.execute( 'SELECT * FROM usr WHERE username = ?', (id,)) 
	return r.fetchone() 

def imprimir_cliente(id):
	if localizar_cliente(id) == None:
		print('Não existe cliente com o id informado.')
	else:
		print(localizar_cliente(id))

localizar_cliente("gusyavos")
imprimir_cliente("GustavinNeh")

print('Tabela criada com sucesso.') # 	desconectando... 
conn.close()


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
	"<p id='tab'>Eu sou o melhor de mim!</p><br>",
	"<p id='tab'>Deixando a vida fluir. Pode levar o que não é para ficar e trazer o que me fará bem.</p><br>",
	"<p id='tab'>Em (re)construção. Ainda bem.</p>"
]

# Já vai inicializando o site.
app = Flask(__name__)
CORS(app)

# Função para gerar um token único para o usuário
def GerarToken():
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
	kk = [
		"hsj",
		"hoe",
		"yei"
	]
	tokenFinal = random.choice(inicio) + random.choice(meio) + random.choice(final)
	return tokenFinal


# Página Inicial
@app.route("/")
def init():
	return render_template("page-init.html")
	
@app.route("/inicio", methods=["GET", "POST"])
def homepage():		
	return render_template('index.html', videos="".join(map(str,videosMaiores)), legendasr="".join(map(str,legendas)))
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
	if request.method == "POST":
		username = request.form["username"]
		plataforma = request.form["plt"]
		print("====> Novo usuário!")
		print("Username: ", username)
		print("Plataforma: ", plataforma)
		print(request.form["token"])
	return render_template("signup.html", token = GerarToken())
	
@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "POST":
		token = request.form["username"]
	
	return render_template("sign-in.html")

@app.route("/settings", methods=["GET", "POST"])
def settings():
	if request.method == "POST":
		nomeUser = request.form["username"]
		plataforma = request.form["plt"]
		senha = request.form["password"]
		print(nomeUser)
		print(plataforma)
		print(senha)
	return render_template("config.html")

@app.route("/api/cadastro", methods=["GET", "POST"])
def cadastrar():
	if request.method == "POST":
		print(request.data)

# Dar run webapp
if __name__ == "__main__":
	app.run(host="0.0.0.0") 