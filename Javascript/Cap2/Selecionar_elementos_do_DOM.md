Para selecionar elementos do DOM em JavaScript, existem várias maneiras, dependendo do critério de seleção que você deseja utilizar. Aqui estão algumas das principais formas de selecionar elementos:

1. Selecionar por ID:
Você pode usar o método `getElementById` para selecionar um elemento pelo seu ID único. Ele retorna o elemento correspondente ou `null` se nenhum elemento for encontrado.

Ver ex1.js

2. Selecionar por classe:
Você pode usar o método `getElementsByClassName` para selecionar elementos por sua classe. Ele retorna uma coleção de elementos correspondentes ou uma coleção vazia se nenhum elemento for encontrado.

Ver ex2.js

3. Selecionar por nome de tag:
Você pode usar o método `getElementsByTagName` para selecionar elementos por seu nome de tag. Ele retorna uma coleção de elementos correspondentes ou uma coleção vazia se nenhum elemento for encontrado.


Ver ex3.js

4. Selecionar por seletor CSS:
Você pode usar o método `querySelector` ou `querySelectorAll` para selecionar elementos com base em um seletor CSS. `querySelector` retorna o primeiro elemento correspondente e `querySelectorAll` retorna uma coleção de todos os elementos correspondentes.


Ver ex4.js

5. Selecionar elementos pai/filho:
Você pode usar as propriedades `parentNode` e `childNodes` para navegar e selecionar elementos pai e filhos de um elemento específico. Por exemplo:


Ver ex5.js

Essas são algumas das principais maneiras de selecionar elementos do DOM em JavaScript. Dependendo do caso de uso e da complexidade da seleção, você pode usar uma ou mais dessas técnicas para obter os elementos desejados.