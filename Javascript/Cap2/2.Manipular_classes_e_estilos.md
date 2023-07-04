A manipulação de classes e estilos é uma parte importante da manipulação do DOM em JavaScript. Ela permite adicionar, remover ou alterar classes CSS em elementos e também modificar os estilos inline dos elementos. Aqui estão algumas maneiras de realizar essa manipulação:

1. Manipular classes:

   - Adicionar uma classe: Para adicionar uma classe a um elemento, você pode usar a propriedade `classList` e o método `add`.
   
   ex6.js

   - Remover uma classe: Para remover uma classe de um elemento, você pode usar o método `remove` da propriedade `classList`.
   
   ex7.js

   - Alternar uma classe: Para alternar a presença de uma classe em um elemento (adiciona se a classe não estiver presente e remove se a classe estiver presente), você pode usar o método `toggle` da propriedade `classList`.
   
   ex8.js

2. Manipular estilos inline:

   - Acesso aos estilos inline: Você pode acessar os estilos inline de um elemento usando a propriedade `style`. Por exemplo, para acessar a cor de fundo de um elemento:
   
   ex9.js

   - Modificar estilos inline: Para modificar os estilos inline de um elemento, você pode usar a propriedade `style` e atribuir um novo valor a uma propriedade CSS específica.
   
   
   ex10.js

   - Atenção: A manipulação de estilos inline usando a propriedade `style` é aplicada diretamente ao elemento em seu atributo `style` e substitui estilos definidos em arquivos CSS externos ou internos.

3. Adicionar e remover várias classes de uma vez:
   - Para adicionar várias classes de uma só vez, você pode usar o método `add` da propriedade `classList` e fornecer várias classes separadas por espaço.
   
   ex11.js

   - Da mesma forma, para remover várias classes de uma só vez, você pode usar o método `remove` da propriedade `classList` e fornecer várias classes separadas por espaço.
   
   ex12.js
   
Essas são algumas maneiras de manipular classes e estilos em JavaScript para modificar a aparência dos elementos do DOM. Essas técnicas permitem que você crie interações dinâmicas e personalizadas em sua página web.