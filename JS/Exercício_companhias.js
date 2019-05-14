class Company{
    constructor(name, year, industry){
        this.name = name
        this.year = year
        this.industry = industry
    }
}

class Companies{
    constructor(companies){
        this.companies = []
    }
    add(company){
        this.companies.push(company)
    }
    foundeAfter(year){
        let yearsAfter = this.companies.filter((elem) => elem.year >= 1995)
        return yearsAfter
    }
    foundBefore(year){
        let yearsBefore = this.companies.filter((elem) => elem.year < 1995)
        return yearsBefore
    }
    show(){
        return this.companies
    }
}

let a = new Company('Google', 1987, 'Internet')
let b = new Company('Amazon', 1985, 'Internet')
let c = new Company('Samsung', 1995, 'Celular')
let d = new Company('Constructor', 2000, 'Programação')

let e = new Companies()

e.add(a)
//e.add(b)
//e.add(c)
//e.add(d)

let teste = e.show()
console.log(teste)