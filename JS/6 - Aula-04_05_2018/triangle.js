///////////////////////
// Classe Triangulo que cria um objeto que representa um Triângulo
//
// Métodos:
//
// isTriangulo() - retorna "true" se os três lados representam um triângulo 
//  e "false" caso contrário
//
// kind() - retorna o tipo do triângulo:
//      3 lados iguais -> equilátero
//      2 lados iguais -> isósceles
//      caso contrário -> escaleno
///////////////////////
class Triangulo{
    constructor(l1,l2,l3){
        this.lados = [l1,l2,l3];
    }
    isTriangulo(){
        let result = true;

        if (this.lados[0] > this.lados[1] + this.lados[2])
            result = false;
        if (this.lados[1] > this.lados[0] + this.lados[2])
            result = false;
        if (this.lados[2] > this.lados[0] + this.lados[1])
            result = false;
            
        return result;
    }
    kind(){

        if (this.lados[0] == this.lados[1] && this.lados[0] == this.lados[2])
            return 'equilatero';
        else if (this.lados[0] == this.lados[1] || this.lados[0] == this.lados[2] || this.lados[1] == this.lados[2])
            return 'isosceles';
        else
            return 'escaleno';
    }
}

let t = new Triangulo(2,1,3);

console.log(t.kind())