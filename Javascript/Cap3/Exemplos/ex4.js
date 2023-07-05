function operacaoAssincrona(callback) {
    setTimeout(function() {
      callback("Dados processados");
    }, 2000);
  }
  
  function callback(resultado) {
    console.log("Resultado: " + resultado);
  }
  
  operacaoAssincrona(callback);  