import sqlite3

class DB:
	def criarUser(username, senha, plt):
		conect = sqlite3.connect("tclientes.db")
		cursor = conect.cursor()
		cursor.execute("""
			INSERT INTO usr (username, senha, plt)
			VALUES (?,?,?)
		""", (username, senha, plt))
		conect.commit()
		conect.close()
	def editarUser(username, senha, plt):
		conect = sqlite3.connect("tclientes.db")
		cursor = conect.cursor()
		cursor.execute(""" 
			UPDATE usr
			SET senha = ?, plt = ?
			WHERE username = ?
		""", (senha, plt, username))
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
		 
	def ValidarUser(token, senha):
		conect = sqlite3.connect("tclientes.db")
		cursor = conect.cursor()
		cursor.execute("SELECT senha FROM usr WHERE username = ?", (token,))
		senhab = cursor.fetchall()
		conect.close()
		if senha == senhab[0][0]:
			return True
		else:
			return False
			
	def Verificar(username):
		conect = sqlite3.connect("tclientes.db")
		cursor = conect.cursor()
		r = cursor.execute("SELECT * FROM usr WHERE username = ?", (username,))
		if r.fetchone() == None:
			return True
		else:
			return False
		
conn = sqlite3.connect("tclientes.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM usr;")
for linha in cursor.fetchall():
	print(linha)

conn.close()