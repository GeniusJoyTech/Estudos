
function operacaoAssincrona() {
    return new Promise(function(resolve, reject) {
      setTimeout(function() {
        resolve("Dados processados");
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
  