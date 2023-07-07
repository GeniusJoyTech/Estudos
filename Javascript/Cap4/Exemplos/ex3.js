var xhr = new XMLHttpRequest();
xhr.open('POST', 'seu_endpoint', true);
xhr.setRequestHeader('Content-Type', 'application/json');

xhr.onload = function() {
  if (xhr.status >= 200 && xhr.status < 400) {
    var data = JSON.parse(xhr.responseText);
    // Faça algo com os dados recebidos
  } else {
    // Trate erros aqui
  }
};

var requestBody = {
  parametro1: valor1,
  parametro2: valor2
};

xhr.send(JSON.stringify(requestBody));
