////////////////
//
// Classe School irá guardar as notas e nomes de alunos por nota em um Object
// 
// O Object terá a seguinte estrutura:
//
//  {
//      1: ["Fulano","Sicrano"],
//      4: ["Beltrano"],
//      6: ["João","Maria"],
//      9: ["Antonio","Pedro"]
//  }
//
// As chaves (1,4,6,9) do Object são as notas dos alunos e cada uma das chaves guarda uma lista de nomes de alunos
////////////////
class School{
    constructor(){
        this.grades = {}; // Object utilizado para guardar as notas e o nome dos alunos
    }
    roster(){
        return this.grades;
    }
    add(student,grade){
        
        if (this.grades[grade] != undefined){ // Se a chave "grade" já existe, adiciona novo aluno
            this.grades[grade].push(student);
            this.grades[grade].sort();
        } else {
            this.grades[grade] = [student]; // Chave inexistente, então cria-se com o primeiro aluno
        }       
    }
    grade(grade){
        if (!this.grades[grade]) // se não existe a chave no Object, retorna lista vazia
            return [];
        else
            return this.grades[grade];
    }
}

let escola = new School();

console.log(escola.roster());

// Adiciona alunos e notas na escola
escola.add("Thiago",9);
escola.add("Pedro",8);
escola.add("Carla",9);
escola.add("Amanda",6);
escola.add("José",6);

// retorna a lista de alunos por nota
console.log(escola.grade(9));
console.log(escola.grade(8));
console.log(escola.grade(6));
console.log(escola.grade(3));
