class Company{

    constructor(name, founded, industry){
        this.name = name;
        this.founded = founded;
        this.industry = industry;
    }

    show(){
        return this.name + " " + this.founded;
    }

}

class Companies{
    constructor(){
        this.companies = [];    
    }
    add(company){
        this.companies.push(company);
    }
    foundedAfter(year){
        return this.companies.filter(c => c.founded >= year)
    }
    foundedBefore(year){
        return this.companies.filter(c => c.founded < year)
    }
    show(){
        let result = "";

        for (let c of this.companies)
            result = result + c.name + " - " + c.founded + "\n";
        
        return result;
    }    
}

let c1 = new Company("Amazon",1995,"Internet");
let c2 = new Company("Google",1998,"Internet");
let c3 = new Company("Apple",1977,"Internet");
let c4 = new Company("Positivo",2000,"Internet");

let listaCompany = new Companies();

listaCompany.add(c1);
listaCompany.add(c2);
listaCompany.add(c3);
listaCompany.add(c4);

let cAfter = listaCompany.foundedAfter(1995);
let cBefore = listaCompany.foundedBefore(1995);

console.log(cAfter);
console.log(cBefore);
console.log(listaCompany.show());