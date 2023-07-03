var meses = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
  ];
  
  var data = new Date();
  var numeroMes = data.getMonth(); // Obtém o número do mês (0-11)
  var nomeMes = meses[numeroMes];
  
  console.log(nomeMes); // Exibe o valor do mês atual  