A manipulação do DOM (Document Object Model) refere-se à capacidade de alterar dinamicamente os elementos e o conteúdo de uma página web por meio de JavaScript. O DOM é uma representação em forma de árvore de todos os elementos HTML em uma página, onde cada elemento é um nó e pode ser manipulado usando métodos e propriedades fornecidos pela API do DOM.

Existem várias maneiras de manipular o DOM usando JavaScript. Aqui estão algumas das operações comuns:

Acesso a elementos: Você pode usar métodos como getElementById, getElementsByClassName e getElementsByTagName para acessar elementos específicos da página.

Modificação de conteúdo: Você pode alterar o conteúdo de um elemento HTML usando a propriedade innerHTML. Por exemplo, document.getElementById('meuElemento').innerHTML = 'Novo conteúdo'; alterará o conteúdo do elemento com o ID "meuElemento".

Modificação de atributos: Você pode alterar os atributos de um elemento HTML usando as propriedades do elemento. Por exemplo, document.getElementById('meuElemento').src = 'nova-imagem.jpg'; alterará o atributo src de uma imagem.

Adição de elementos: Você pode adicionar novos elementos ao DOM usando métodos como createElement e appendChild. Por exemplo, o código a seguir cria um novo parágrafo e o adiciona ao final do corpo do documento:

ex20.js

Remoção de elementos: Você pode remover elementos do DOM usando o método removeChild. Por exemplo, var elementoRemovido = document.getElementById('meuElemento').parentNode.removeChild(document.getElementById('meuElemento')); remove o elemento com o ID "meuElemento" do seu pai.