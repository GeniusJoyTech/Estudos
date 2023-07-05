function operacaoAssincrona() {
  return new Promise(function(resolve, reject) {
    setTimeout(function() {
      // Simulando uma operação assíncrona bem-sucedida
      resolve("Dados processados");
      // Ou, para simular uma falha:
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
