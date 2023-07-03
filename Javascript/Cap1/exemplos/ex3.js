// Tipos primitivos
var string = "Olá, mundo!";      // String
var number = 42;                 // Number
var boolean = true;              // Boolean
var nulo = null;                 // Null
var indefinido = undefined;      // Undefined
var symbol = Symbol("chave");    // Symbol


// Objetos
var array = [1, 2, 3];           // Array
var objeto = {                   // Object
  nome: "João",
  idade: 25,
  profissao: "programador"
};
var funcao = function() {        // Function
  console.log("Isso é uma função");
};

//Tipos adicionais

var numeroGrande = 1234567890123456789012345678901234567890n; // BigInt
var dataAtual = new Date(); // Date
var expressaoRegular = /[A-Za-z]+/; // RegExp

console.log(string);
console.log(number);
console.log(boolean);
console.log(nulo);
console.log(indefinido);
console.log(symbol);
console.log(array);
console.log(objeto);
console.log(funcao);
console.log(numeroGrande);
console.log(dataAtual);
console.log(expressaoRegular);
