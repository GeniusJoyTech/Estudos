var xhr = new XMLHttpRequest();
xhr.open('GET', 'seu_endpoint?parametro1=valor1&parametro2=valor2', true);

xhr.onload = function() {
  if (xhr.status >= 200 && xhr.status < 400) {
    var data = JSON.parse(xhr.responseText);
    // Faça algo com os dados recebidos
  } else {
    // Trate erros aqui
  }
};

xhr.send();
