

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

async function Face() {
  let response = await fetch("https://graph.facebook.com/v14.0/me?fields=id%2Cname&access_token=EAAURMmzG7MgBAEohFBqktDyNGqlZAL1umgCEUAkXiR2rGRsBFg9bvYijbC9CYZBNtmKbp25uyiGS2X7Ro8MLNLN5lKx5hAOvQuGUf1JM0yPsqcWvy51wHzDyQB361ZC6BeW4YtR5ZAjkKLCgAeExeWSYx2m31ZBAKD9SN1g7RVTZB6ymZCv0mUBkSwzcHsb9K1OvjHXls1E5wZDZD")
  const data = response
  console.log(data)
}

Face()
