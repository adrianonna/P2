
/////////////
//
// Métodos de STRING
//
/////////////
let frase = "Descobri que quanto mais eu estudo, mais sorte eu pareço ter nas provas";

//console.log(arrayFrase.slice(2,5)); // Gera novo Array

console.log(frase.length);
console.log(frase.toUpperCase()); // Gera um String
console.log(frase.toLowerCase()); // Gera um String
console.log(frase.split(" ")); // Gera um Array

let arrayFrase = frase.split(" ");

/////////////
//
// Métodos de ARRAY
//
/////////////
console.log(arrayFrase.join(" ")); // Gera um String
console.log(arrayFrase.reverse()); // Altera o array
console.log(arrayFrase.reverse()); // Altera o array

console.log(arrayFrase.slice(2,5)); // Gera novo Array

/////////////
//
// Métodos de String = replace(), substr()
//
/////////////
let novaFrase = "Aquele que não luta pelo futuro que quer, deve aceitar o futuro que vier";

console.log(novaFrase.replace('e','?')); // Gera nova String
console.log(novaFrase.substr(3,5)); //index = 3, caracteres = 5 - Nova String
console.log(novaFrase.substring(3,5)); //indexInicial = 3, Até o 5 elemento da String - Nova String
console.log(novaFrase.substring(3)); //indexInicial = 3 - Nova String

//////////////////////
// Trocar todos os caracteres de uma String, por outro
//////////////////////
while (novaFrase.search('e') != -1)
    novaFrase = novaFrase.replace('e','X');

console.log(novaFrase);

//////////////////////
// Usando Regex para trocar todos os caracteres encontrados por outro
//////////////////////
let novaFrase2 = "Aquele que não luta pelo futuro que quer, deve aceitar o futuro que vier";

console.log(novaFrase2.replace(/e/g,"?")); // Trocar em todas as ocorrências


//////////////////////
// Exercício: Imprimir o nome e e-mail da pessoa
//////////////////////
const name = `student: Alice; email: alice@email.com`

let arrayName = name.split(' ');

result = arrayName[1] + ' ' + arrayName[3];

//////////////////////
// Exercício: Imprimir todos os nomes e e-mails
//////////////////////
const names = `student: Alice; email: alice@email.com student: Bob; email: bobbob@email.com student: Charlie; email: charlie@email.com`

let arrayNames = names.split(' ');

console.log(arrayNames.filter((e, i) => i % 2 != 0))