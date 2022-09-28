def GiveResult(NumeroSeguidores, Engajamento, ContasAlcancadas):
	# Variaveis com as opiniões
	OpnSeguidores = ""
	OpnEngajamento = ""
	OpnAlcance = ""
	OpnFinal = ""
	
	# Receber As Opinioes com os dados
	
	# Número de seguidores
	
	if NumeroSeguidores < 500:
		OpnSeguidores = "Seus seguidores ainda estão muito pouco. Melhore-os, faça vídeos com edições tops e crie um cronograma semanal de postagem de conteúdo."
	if NumeroSeguidores >=500 and NumeroSeguidores < 800:
		OpnSeguidores = "Seus número de seguidores tá bem top, mas precisa melhorar, faça no máximo 2 vídeos por dia. Chame seus amigos para repostar seus vídeos, ou escolha uma categoria principal para seu perfil, Ex.: Comédia, Motivacional etc."
	if NumeroSeguidores >= 800 and NumeroSeguidores < 1100:
		OpnSeguidores = "Seus números de seguidores estão bons, sua missão agora é não perder esses seguidores, mas faça seu perfil melhorar, crie Reels, poste no máximo 5 storys por dia, e poste coisas engraçadas, use filtros mais simples. E poste vídeos entre 11h até 12h ou 18h até 19h"
	if NumeroSeguidores >= 1100:
		OpnSeguidores = "Seu número de seguidores estão ótimos! Parabéns! Mas continue melhorando, peça para seus conhecidos divulgar vídeos seus nos story deles. <strong>'time que tá bom não se meche'</strong>"
		
	# Engajamento
	if Engajamento < 40:
		OpnEngajamento = "Seu engajamento está ruim, mas pode melhorar! Coloque figurinhas de reações nos seus storys, coloque nas legendas tipo assim: <strong>o horário que voce está vendo este vídeo é a idade de um casal, coloque nos comentários ksks</strong>."
	if Engajamento >= 40 and Engajamento < 80:
		OpnEngajamento = "Seu engajamento nao está muito bom, mas pode melhorar, crie algo original seu, por exemplo, crie um vídeo original e uma hashtag original para esse vídeo, e poste na plataforma de chat do KyVolution para inspirar outros criadores de vídeo e fazer seu vídeo ter maior alcance."
	if Engajamento >= 80 and Engajamento < 120:
		OpnEngajamento = "Seu engajamento tá top, mas pode melhorar, coloque legendas que façam o telespectador comentar seu vídeo ou story. Ex.: <strong>Quantos K voce consegue digitar sem respirar? Teste nos comentários</strong>."
	if Engajamento >= 120 and Engajamento < 200:
		OpnEngajamento = "Seu engajamento tá bom, se quiser pode até fazer o mesmo método que está fazendo atualmente. Mas se quiser melhorar, faça as pessoas comentar e interagir nos seus conteúdos, faça umas brincadeiras nos storys."
	if Engajamento >= 200:
		OpnEngajamento = "Seu engajamento tá ótimo!"
		
	# Contas Alcançadas
	if ContasAlcancadas < 30:
		OpnAlcance = "Seu número de contas alcançadas está ruim, mas pode melhorar, poste no máximo 1 vídeo por dia, e coloque hashtags que tenham haver com o tema do seu vídeo. E crie vídeos sobre algum tema que o povo queira ver, voce pode usar o Google Trends para ver os temas mais buscados do dia, ou use o próprio Instagram para ver temas mais buscados, olhe o explorer, vai que lá tenha um tema top, mas no KyVolution, na página inicial tem as ideias de vídeos para voce criar."
	if ContasAlcancadas >= 30 and ContasAlcancadas < 70:
		OpnAlcance = "Seu alcance está até bom, use as idéias de vídeos da KyVolution, use as hashtags que tenham haver com o vídeo, e se possível crie mais vídeos Reels, mas poste no máximo 2 por dia."
	if ContasAlcancadas >= 70 and ContasAlcancadas < 140:
		OpnAlcance = "Seu alcance está top, mas pode melhorar, crie uma boa relação com seus usuários nos comentários, sempre responda os comentários com maior educação e faça com que o usuário curta seu perfil e volte mais vezes, se quiser relembre vídeos do passado que deram certo e reposte. Crie conteúdos originais! As vezes as Idéias de vídeos do KyVolution são originais!"
	if ContasAlcancadas >= 140:
		OpnAlcance = "Seu número de contas alcançadas tá top! Mas se quiser melhorar, crie mais engajamento, e crie vídeos que façam os usuários marcar um amigo, de opiniões ou algo do tipo!"
	# Fim dos relatórios
	
	# Começo das Opiniões finais
	lista = []
	lista.append(f"<li class='list-group-item'>{OpnSeguidores}</li>")
	lista.append(f"<li class='list-group-item'>{OpnAlcance}</li>")
	lista.append(f"<li class='list-group-item'>{OpnEngajamento}</li>")
	print(lista)
	# Bloco de código.
	blocoDeCodigoHtml = """ 
	  <div style="color: #000;" class="container">
      	<ul class="list-group list-group-flush">
      		{}
      	</ul>
      </div>
	""".format("".join(map(str, lista)))
	print(blocoDeCodigoHtml)
	return blocoDeCodigoHtml
	

		
	
	