# imports e conjuntos em funcoes
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import Trends
import Legends

# app
app = Flask(__name__)

# cors
CORS(app)
# as páginas
@app.route("/")
def homepage():
  return render_template("index.html")

@app.route("/insights")
def insightsp():
  return render_template("insights.html")

@app.route("/login")
def loginp():
  return render_template("login.html")

@app.route("/cadastro")
def cadastro():
  return render_template("cadastro.html")

# API's
#lançar o site
if __name__ == '__main__':
  app.run(host='0.0.0.0')