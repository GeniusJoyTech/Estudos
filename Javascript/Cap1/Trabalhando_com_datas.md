Ao trabalhar com datas em JavaScript, você pode usar o objeto embutido `Date`. Ele fornece uma variedade de métodos para criar, manipular e formatar datas. Aqui estão algumas operações comuns para trabalhar com datas no JavaScript:

1. Criando um objeto `Date`:
   Você pode criar um objeto `Date` de várias maneiras. Aqui estão alguns exemplos:

  Ver ex4.js
  
2. Obtendo informações da data:
   O objeto `Date` possui métodos para obter informações específicas da data, como ano, mês, dia, hora, minuto, segundo, etc. Aqui estão alguns exemplos:

Ver ex5.js


3. Manipulando datas:
   O objeto `Date` permite manipular datas adicionando ou subtraindo dias, meses, anos, etc. Aqui estão alguns exemplos:

Ver ex6.js

4. Comparando datas:
   Para comparar datas, você pode usar os operadores de comparação (`<`, `<=`, `>`, `>=`) ou comparar os valores retornados pelos métodos `getTime()` dos objetos `Date`. O método `getTime()` retorna o valor numérico correspondente à data em milissegundos desde 1º de janeiro de 1970.

   Ver ex7.js


5. Formatação de datas:
   O JavaScript não possui um método nativo para formatar datas, mas você pode criar sua própria função ou usar bibliotecas como o Moment.js ou o Intl.DateTimeFormat para formatar datas em diferentes formatos.

Ver ex8.js

Para transformar o número do mês em um valor de mês legível, você pode criar um array com os nomes dos meses e usar o número do mês como índice para obter o valor correspondente.  Aqui está um exemplo:

Ver ex9.js

Neste exemplo, criamos um array chamado meses que contém os nomes dos meses. Em seguida, usamos o método getMonth() do objeto Date para obter o número do mês atual (0-11). Em seguida, usamos esse número como índice para acessar o valor correspondente no array meses.

Dessa forma, o código exibirá o valor do mês atual de forma legível. Por exemplo, se o número do mês for 6, o código exibirá "Julho".