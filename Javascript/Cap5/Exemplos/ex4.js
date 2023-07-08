document.getElementById("meuFormulario").addEventListener("submit", function(event) {
  event.preventDefault(); // Impede o envio do formulário padrão

  var formData = new FormData(this); // Captura os dados do formulário

  // Envie os dados usando uma requisição AJAX ou outra técnica de envio
  enviarDados(formData);
});

function enviarDados(formData) {
  // Use uma requisição AJAX para enviar os dados do formulário
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "url_do_destino");
  xhr.send(formData);

  // Lógica para tratar a resposta da requisição
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        console.log("Dados enviados com sucesso!");
        // Adicione o código adicional aqui para lidar com a resposta da requisição
      } else {
        console.log("Erro ao enviar dados. Código de status: " + xhr.status);
        // Adicione o código adicional aqui para lidar com erros de envio
      }
    }
  };
}
