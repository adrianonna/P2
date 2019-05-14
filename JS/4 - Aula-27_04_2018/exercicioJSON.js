////////////////
// Object.keys(obj) – retorna um array de chaves
// Object.values(obj) – retorna um array de valores
// Object.entries(obj) – retorna um array de [chave,valor]
////////////////

const post = {
    title: 'lorem ipsum dolor',
    text: 'Nunc accumsan in ipsum a mattis...',
}

// console.log(Object.keys(post))
// console.log(Object.values(post))
// console.log(Object.entries(post))

/////////////////////////
// Exercício de Companies
/////////////////////////
const companies = [
    {
      name: 'Amazon',
      founded: 1994,
      industry: 'E-Commerce, Cloud',
    },
    {
      name: 'Alphabet Inc.',
      founded: 2015,
      industry: 'Search, Cloud, Advertising',
    },
    {
      name: 'Facebook',
      founded: 2004,
      industry: 'Social',
    }
  ]

  // for (let company of companies)
  //   for (let values of Object.values(company))
  //       console.log(values)


//console.log(Object.keys(companies))
//console.log(Object.values(post))
//console.log(Object.entries(companies))


//////////////////
// Duas formas de fazer!
//////////////////
for (let index in companies)
    companies[index].kind = "Internet company"

//console.log(companies)

for (let elem of companies)
    elem.kind = "Internet company"

// /////// FORMA 1
// console.log("--- FORMA 1 ---")
// for (let index in companies)
//     console.log(companies[index].name + " - " + companies[index].founded)
    
// /////// FORMA 2
// console.log("--- FORMA 2 ---")
// for (let index of Object.keys(companies))
//     console.log(companies[index].name + " - " + companies[index].founded)

// /////// FORMA 3
// console.log("--- FORMA 3 ---")
// for(let [key,value] of Object.entries(companies))
//     console.log(value.name + " - " + value.founded)

// /////// FORMA 4
// console.log("--- FORMA 4 ---")
// for(let value in Object.values(companies))
//     console.log(companies[value].name + " - " + companies[value].founded)


// ////////////////////////
// // Exercício de Produtos
// ////////////////////////
let produtos = [
   {
     nome: 'Bicicleta',
     preco: 1200.0
   },
    {
      nome: 'Capacete',
      preco: 450.0
    }
  ]

let result = produtos.reduce((soma, elem) => soma + elem.preco,0);

console.log(result)