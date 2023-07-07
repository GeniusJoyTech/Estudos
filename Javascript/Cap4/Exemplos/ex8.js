var data = {
    nome: 'John Doe',
    idade: 30,
    email: 'johndoe@example.com'
  };
  
  fetch('https://api.exemplo.com/usuarios', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(result => {
    console.log('Usuário criado:', result);
  })
  .catch(error => {
    console.error('Erro:', error);
  });
  