
def Relatorio(engajamento, contas_alcancadas, seguidores):
	mensagens1 = ""
	mensagens2 = ""
	mensagens3 = ""
	if engajamento <= 50:
		mensagens1 = "Seu engajamento está ruim, crie vídeos com base no cotidiano no Brasileiro, por exemplo: Quando meu celular descarrega e preciso dele. Faça o pessoal dar risada e comentar e curtir os seus vídeos!"
	if engajamento > 51 and engajamento < 99:
		mensagens1 = "Seu engajamento não está ruim, mas pode melhorar, crie vídeos que faça o pessoal se divertir e comentar em seus vídeos!"
	if engajamento >= 100:
		mensagens1 = "Seus número de engajamento estão ótimos!"
	if contas_alcancadas <= 150:
		mensagens2 = "Seus números de contas alcançadas não estão bons, coloque em seus vídeos as hashtag: #trending e mais umas 3 hashtags que sejam do tema do seu vídeo!"
	if contas_alcancadas > 151 and contas_alcancadas < 499:
		mensagens2 = "Seu número de contas alcançadas não está ruim, mas voce pode melhorar: Coloque palavras chaves na descrição do vídeo, coloque no máximo 3 hashtag e inclua: #trending, e se puder peça a familiares ou amigos repostarem seu melhor vídeo!"
	if contas_alcancadas > 500:
		mensagens2 = "Seu número de contas alcançadas estão ótimos!"
	if seguidores <= 500:
		mensagens3 = "Seu número de seguidores está muuito baixo! Veja como melhorar: Poste no máximo 2 vídeos por dia, e pelo menos 5 toda semana, use as Dicas Do Dia - Vídeos.!"
	if seguidores > 501 and seguidores < 799:
		mensagens3="Seu número de seguidores não está ruim, mas poste vídeos entre: 10h até 12h, e tb 18h até 19h, coloque legendas com palavras chaves do seu vídeo!"
	if seguidores > 800:
		mensagens3="Seu número de seguidores está ótimo!"
	opn = [
		"<br>1. "+mensagens1 + "<br>",
		"2. "+mensagens2+"<br>",
		"3. "+mensagens3
	]
	return opn

