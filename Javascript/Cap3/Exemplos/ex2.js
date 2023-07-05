function operacaoAssincrona() {
    return new Promise(function(resolve, reject) {
      setTimeout(function() {
        resolve("Dados processados");
        // reject("Ocorreu um erro");
      }, 2000);
    });
  }
  
  operacaoAssincrona()
    .then(function(resultado) {
      console.log("Resultado: " + resultado);
    })
    .catch(function(erro) {
      console.log("Erro: " + erro);
    });
  
