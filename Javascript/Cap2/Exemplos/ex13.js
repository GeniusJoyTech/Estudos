// Criar um novo elemento
var novoElemento = document.createElement('div');
novoElemento.textContent = 'Novo elemento';

// Selecionar o elemento pai onde deseja adicionar o novo elemento
var elementoPai = document.getElementById('elementoPai');

// Adicionar o novo elemento ao elemento pai
elementoPai.appendChild(novoElemento);

// Remover o elemento adicionado
elementoPai.removeChild(novoElemento);
