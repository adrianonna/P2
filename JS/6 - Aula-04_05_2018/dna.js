class DnaTranscriber {

   constructor(){
        this.complemento = {
            'G': 'C',
            'C': 'G',
            'T': 'A',
            'A': 'U'
        }
  
  }
  
  toRna(dna) {
    
    return dna
      .split('')
      .map(elem => this.complemento[elem])
      .join('')
  }

}

const dnaTranscriber = new DnaTranscriber()
console.log(dnaTranscriber.toRna('C')) //=> G
console.log(dnaTranscriber.toRna('G')) //=> C
console.log(dnaTranscriber.toRna('A')) //=> U
console.log(dnaTranscriber.toRna('T')) //=> A
console.log(dnaTranscriber.toRna('ACGTGGTCTTAA')); //=> UGCACCAGAAUU



let minhaString = "2018";

let meuObjeto = 
{
  "1" : 'um',
  "2" : 'dois',
  "3" : 'tres',
  "4" : 'quatro',
  "5" : 'cinco',
  "6" : 'seis',
  "7" : 'sete',
  "8" : 'oito',
  "9" : 'nove',
  "0" : 'zero'
}

let meuArrayQuadrado = minhaString.split('').map(elem => meuObjeto[elem]).join(' ');

console.log(meuArrayQuadrado);