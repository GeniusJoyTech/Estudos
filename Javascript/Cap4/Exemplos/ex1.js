var xhr = new XMLHttpRequest();
xhr.open('GET', 'seu_endpoint', true);

xhr.onload = function() {
  if (xhr.status >= 200 && xhr.status < 400) {
    var data = JSON.parse(xhr.responseText);
    // Faça algo com os dados recebidos
  } else {
    // Trate erros aqui
  }
};

xhr.send();