var data = JSON.parse(xhr.responseText);
document.getElementById('elemento').textContent = data.valor;
