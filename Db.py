import sqlite3

class DB:
	def criarUser(username, senha, plt):
		conect = sqlite3.connect("tclientes.db")
		cursor = conect.cursor()
		cursor.execute("""
			INSERT INTO usr (username, senha, plt)
			VALUES (?,?,?,?)
		""", (username, senha, plt))
		conect.commit()
		conect.close()
	def editarUser(username, senha, plt):
		conect = sqlite3.connect("tclientes.db")
		cursor = conect.cursor()
		cursor.execute(""" 
			UPDATE usr
			SET senha = ?
			SET plt = ?
			WHERE username = ?
		""", (username, senha, plt))
		conect.commit()
		conect.close()
	
	def excluir(token):
		conect = sqlite3.connect("tclientes.db")
		cursor = conect.cursor()
		cursor.execute("""
			DELETE FROM usr WHERE username = ?
		 """, (token))
		conect.commit()
		conect.close()
		 
	def ValidarUser(token, senha, plt):
		conect = sqlite3.connect("tclientes.db")
		cursor = conect.cursor()
		cursor.execute("SELECT senha FROM usr WHERE username = ?", (token))
		senhab = cursor.fetchall()
		cursor.execute("SELECT plt FROM usr WHERE username = ?", (token))
		pltd = cursor.fetchall()
		conect.close()
		if senha == senhab[0][0] and plt == pltd[0][0]:
			return True
		else:
			return False
			
	def Verificar(token):
		pass