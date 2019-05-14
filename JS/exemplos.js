let list = [1,2,3,4,5,6,7,8]
let x = list.filter((valor, indice, array) => valor > 4) //valor, indice e array são parâmetros de filter ou uma função anônima? É uma função passada por parâmetro
let y = list.filter((valor, indice, array) => valor >= 2)
console.log(x)
console.log(y)
list = list.filter((valor, indice, array) => valor > 2) //Filtra e altera lista
console.log(list)
d = list.map((valor, indice, array) => { //percorre os valores
    if (valor == 4){ //altera o valor que for igual a 4
        valor = 2
    }if (indice == 0){ //altera o valor do indice que for igual a 0
        valor = 1
    }console.log(valor)
    })
console.log(list) //pq deu underfined? Como altero permanente o valor da lista

list = [{item: 1}, {item: 2}, {item: 3}, {item: 4}]
console.log('list =')
console.log(list) //pq está aparecendo o item name se ainda não adicionei?
let a = list.filter((valor, indice, array) => valor.item >= 2) //filtra os objetos com valor do item >= 2
console.log('a =')
console.log(a)
console.log('b =')
let b = list.map((valor, indice, array) => {
        valor.name = 'Ada' //adiciona mais um item(name) com valor(Adriano) a cada objeto
        console.log(valor) //printa cada objeto
        return valor
    })
console.log(b)
let c = list.map((valor, indice, array) => {
        valor.name = 'Adriano' //altera a valor de name 'Ada' para 'Adriano'
        //console.log(valor) printa cada objeto
        if (indice == 3){
            valor = 28 //altera o valor do indice 3 para 28
        }
        return valor
    })
console.log('c =')
console.log(c)


let A = 10
let B = 1
let C = 12
if (A > B && A > C) // || ou
console.log(A + ' eh o maior');
else if (B > C && B > A)
console.log(B + ' eh o maior');
else if (C > A && C > B)
console.log(C + ' eh o maior');


const frase = 'Student: Adriano; email: adriano_amaral@msn.com; student: adriano'
let name1, name2, name3, name4, name5 
name1 = frase.split(' ')//separa por elementos onde encontrar o parâmetro informado, no caso o espaço em branco
name2 = name1.join(' separador ')//junta os elementos separando-os pelo parâmetro ou sem parâmetro
console.log(name2)
name3 = name1.slice(1, 4)//retorna uma lista com os elementos dos índices indicados(esquerda para direita)
console.log(name3)
name3 = name1.slice(-4, -2)//retorna uma lista com os elementos dos índices invertidos(direita para esquerda)
console.log(name3)
name4 = frase.replace('email', 'endereço eletrônico')
console.log(name4)
console.log(frase.replace(/student/gi, 'aluno'))//Troca todos os nomes student para aluno, maiúculo ou minúsculo
console.log('O índice de "adriano" ou "Adriano" é '+frase.search(/adriano/i))//retorna o primeiro índice onde encontrar "adriano" ou "Adriano"
console.log('O índice de "adriano" é '+frase.search(/adriano/))//retorna o primeiro índice onde encontrar "adriano"
name1 = name1[1] + ' ' + name1[3]
console.log(name1)


const characters = [
{
comics: 'Marvel',
height: 1.78,
name: 'Spider-Man'
},
{
comics: 'Marvel',
height: 2.44,
name: 'Hulk'
},
{
comics: 'DC',
height: 1.91,
name: 'Superman'
},  
{
comics: 'DC',
height: 1.88,
name: 'batman'
}
]
let resultado = characters.reduce((soma, valor) => soma + valor.height, 0)
console.log(resultado / characters.length) //=> 2.0025
let resultado2 = characters.filter((elemento) => elemento.comics === 'DC').reduce((soma, valor) => soma + valor.height, 0)
let aux = characters.filter((elemento) => elemento.comics === 'DC')
let resultado3 = characters.reduce((soma, valor) => valor.comics === 'DC') //Retorna True pq?
console.log(resultado3)
console.log(resultado2 / aux.length) //=> 1.895


class Point{
    constructor(x, y){
        this.x = x
        this.y = y
    }
}
let p1 = new Point(0, 0)
let p2 = new Point(1, 0)
let p3 = new Point(1, 1)
console.log(p1)


class Mamifero{
    constructor(sound){
        this.sound = sound
    }
    talk(){
        return this.sound
    }
}
class Dog extends Mamifero{
    constructor(){
        super('woffeliwofffffffff')
    }
}
let ex1 = new Mamifero('woof')
console.log(ex1)
let ex2 = new Dog()
let ex3 = ex2.talk()
console.log(ex2)
console.log(ex3)
ex2.sound = 'Miau'
console.log(ex2)
console.log(ex3)


class Robo{
    constructor(nome){
        this.nome = nome
    }
    andar(){
        console.log(this.nome + 'está andando')
    }
    falar(){
        console.log(this.nome + 'está falando')
    }
    parar(){
        console.log(this.nome + 'está parando')
    }
    static metodoEstatico(){
        console.log('Método estático executando')
    }
}
class MeuRobo extends Robo{
    pular(){
        console.log(this.nome + 'está pulando')
    }
}
Robo.metodoEstatico()
//let Robo1 = new Robo('R2D2')
let Robo1 = new MeuRobo('C3P0')//herança de Robo
Robo1.andar()
Robo1.falar()
Robo1.parar()
Robo1.pular()