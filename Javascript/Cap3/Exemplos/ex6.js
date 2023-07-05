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
  
  async function executarOperacao() {
    try {
      const resultado = await operacaoAssincrona();
      console.log("Resultado: " + resultado);
    } catch (erro) {
      console.log("Erro: " + erro);
    }
  }
  
  executarOperacao();
  