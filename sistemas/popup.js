class PopUp {
  constructor() {
    this.body = document.querySelector("body")
  }
  
  popUp(title, html) {
    document.getElementById("bodyo").style.opacity="4%"
    var divA = document.getElementById("popup")
    divA.style.opacity='100%'
    divA.innerHTML= `
      <h2>${title}</h2>
      ${html}
      <br>

    `
    document.getElementById("close").addEventListener('click', function() {
  divA.style.opacity="0%"
  document.getElementById("bodyo").style.opacity="100%"
  divA.innerHTML=""
  })
 }
 closePop() {
   document.getElementById("close").addEventListener('click', function() {
  divA.style.opacity="0%"
  document.getElementById("bodyo").style.opacity="100%"
  divA.innerHTML=""
  })
 }
}
