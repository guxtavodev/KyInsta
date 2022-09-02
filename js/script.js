function CriarReplie(comment, answer) {
  pp.popUp("Criar Resposta", `
    <label>Qual vai ser a resposta?: </label> <input id="prg" type="text"> <br>
    <label>Qual vai ser a resposta?: </label>
    <input type="text">
    <a id='pr'><button class="pr" id="close">Ok</button></a>
    <script>
  `)
  document.getElementById("pr").addEventListener('click', function() {
  console.log(document.getElementById("prg").value)
})
}

const pp = new PopUp()

/* async function Teste() {
  try {
    const response = await fetch("http://192.168.0.6:5000")
    console.log(response)
    const data = await response.json()
    console.log(data)
  } catch(error) {
    console.log(error)
  }
}

Teste()*/


