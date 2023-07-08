var campoEmail = document.getElementById("email");
if (campoEmail.validity.valid) {
  console.log("Email válido");
} else {
  console.log("Email inválido");
}