// class Triangulo{
//     constructor(lado1, lado2, lado3){
//         this.lados = [lado1, lado2, lado3]
//     }

//     tipo(){
//         if (this.lados[0] == this.lados[1] && this.lados[0] == this.lados[2] && this.lados[1] == this.lados[2]){
//             return 'Equilátero'
//         }
//         else if (this.lados[0] == this.lados[1] || this.lados[1] != this.lados[2] || this.lados[0] == this.lados[2]){
//             return 'Isósceles'
//         }
//         else if (this.lados[1] != this.lados[2] && this.lados[1] != this.lados[0] && this.lados[0 != this.lados[2]]){
//             return 'Escaleno'
//         }
//         else return 'Não é triângulo'
//     }

//     eTriangulo(){
//         if (this.lados[0] > this.lados[1]*2 || this.lados[0] > this.lados[2]*2){
//             return true
//         }
//         else if (this.lados[1] > this.lados[0]*2 || this.lados[1] > this.lados[2]*2){
//             return true
//         }
//         else if (this.lados[2] > this.lados[1]*2 || this.lados[2] > this.lados[0]*2){
//             return true
//         }
//         else return false
//     }
// }

// let a, b, c
// a = new Triangulo(2, 2, 2)
// b = new Triangulo(1, 2, 1)
// c = new Triangulo(5, 2, 2)
// console.log(a.tipo())
// console.log(a.eTriangulo())
// console.log(b.tipo())
// console.log(b.eTriangulo())
// console.log(c.tipo())
// console.log(c.eTriangulo())


// class Escola{
//     constructor(){
//         this.grades = {}
//     }

//     add(nome, nota){
//         if (this.grades[nota] == undefined){
//             this.grades[nota] = [nome]
//         }
//         else this.grades[nota].push(nome)
//     }

//     nomes(nota){//retorna o array de nomes com essa nota
//         return console.log(this.grades[nota])
//     }
// }

// let a, b, c
// a = new Escola()
// a.add('Adriano', 10)
// b = new Escola()
// b.add('Pedro', 7)
// c = new Escola()
// c.add('Carol', 2)

// a.nomes(10)

class Senha{
    constructor(frase){
        this.frase = frase
    }

    desCrip(frase){
        
    }
}