document.getElementById("meuFormulario").addEventListener("submit", function(event) {
    event.preventDefault(); // Impede o envio do formulário padrão
  
    // Chame as funções de validação para cada campo do formulário
    if (validarNome() && validarEmail() && validarSenha()) {
      // O formulário é válido, você pode enviar os dados ou executar outras ações aqui
      console.log("Formulário válido!");
      // Adicione o código adicional aqui para enviar os dados ou executar ações adicionais
    }
  });
  
  function validarNome() {
    var nome = document.getElementsByName("nome")[0].value;
  
    if (nome.length === 0) {
      alert("Por favor, preencha o campo Nome.");
      return false;
    }
  
    // Adicione mais condições de validação conforme necessário
  
    return true;
  }
  
  function validarEmail() {
    var email = document.getElementsByName("email")[0].value;
  
    if (email.length === 0) {
      alert("Por favor, preencha o campo E-mail.");
      return false;
    }
  
    // Adicione mais condições de validação conforme necessário
  
    return true;
  }
  
  function validarSenha() {
    var senha = document.getElementsByName("senha")[0].value;
  
    if (senha.length === 0) {
      alert("Por favor, preencha o campo Senha.");
      return false;
    }
  
    // Adicione mais condições de validação conforme necessário
  
    return true;
  }
  