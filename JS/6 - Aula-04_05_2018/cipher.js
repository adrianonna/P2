///////////////////////////
//
// rotate() recebe o valor de rotação dos caracteres, ex. 3 (ROT3), 13 (ROT13)
//
// Exemplo:
//
// let texto = ['A','l','o',' ','M','u','n','d','o']
//
// Executa => texto.rotate(3);
//
// this.slice(3, 9) => [' ','M','u','n','d','o']
// .concat(this.slice(0, 3)); => ['A','l','o']
//
// Resultado Final:
//=> [ ' ', 'M', 'u', 'n', 'd', 'o', 'A', 'l', 'o' ]
//
///////////////////////////
Array.prototype.rotate = function(n) {
    return this.slice(n, this.length).concat(this.slice(0, n));
}

class Cipher {

  complement(rotate){
    let complement = {};  // a saída é um objeto complemento onde cada caractere é é substituído por outro na rotação
    let inputChars = 'abcdefghijklmnopqrstuvwxyz'.split(''); // separa todos os caracteres criando um Array
    let outputChars = inputChars.rotate(rotate); // rotaciona o alfabeto

    let index = 0;
    for (let char of inputChars){ // monta o objeto complemento { 'a':'d','A':'D','b':'e','B':'E'}
        complement[char.toLowerCase()] = outputChars[index].toLowerCase();
        complement[char.toUpperCase()] = outputChars[index].toUpperCase();
        index++;
    }

    return complement;
  }

  rot(str, rotate=13) {
    
    let substitution = this.complement(rotate);

    return str
        .split('')
        .map(char => substitution[char] ? substitution[char] : char) // se substitution[char] => undefined, usa o próprio caractere
        .join('');
 }

}

let cifra = new Cipher();

let mensagem1 = "Qrfpboev dhr dhnagb znvf rh rfghqb, znvf fbegr rh cnerçb gre anf cebinf";
let mensagem2 = "Aãb vzcbegn b dhãb qrintne ibpê iá, qrfqr dhr ibpê aãb cner";

console.log(cifra.rot(mensagem1));
console.log(cifra.rot(mensagem2));














    // inputChars.forEach((char, index) => { // monta o objeto complemento { 'a':'d','b':'e'}
    //     complement[char.toLowerCase()] = outputChars[index].toLowerCase();
    //     complement[char.toUpperCase()] = outputChars[index].toUpperCase();
    // });
