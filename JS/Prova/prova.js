//PRIMEIRA QUESTÃO!!!
let primeira = function(financiamento, juroMensal, meses){
    //let resultado = (financiamento*juroMensal)/(1-(1/((1+juroMensal)**meses)))
    //return resultado

    let cal1 = financiamento*juroMensal
    let cal2 = 1-(1/(Math.pow(1+juroMensal, meses)))
    let resultado = cal1 / cal2
    return resultado
}
console.log(primeira(20000, 1.82, 36)) //=> 27437.565620289548
console.log(primeira(20000, 1.82, 24)) //=> 24863.60444684676
console.log(primeira(20000, 1.82, 12)) //=> 22444.174290541192




//SEGUNDA QUESTÃO!!!
let segunda = function(valorInicial, aporte, juroMensal, meses){
    let calc1 = valorInicial*Math.pow(1+juroMensal, meses)
    let calc2 = (aporte*(Math.pow(1+juroMensal, meses)-1))/juroMensal
    let resultado2 = calc1 + calc2
    return resultado2
}
console.log(segunda(100, 500, 0.5936, 12)) //=> 6307.176654943719
console.log(segunda(100, 500, 0.5936, 24)) //=> 12971.227695545636
console.log(segunda(100, 500, 0.5936, 36)) //=> 20125.781003832304
console.log(segunda(100, 500, 0.5936, 120)) //=> 87335.08961181375




//TERCEIRA QUESTÃO!!!
const ipca = {
    '2018': [0.29, 0.32, 0.09, 0.22],
    '2017': [0.38, 0.33, 0.25, 0.14, 0.31, -0.23, 0.24, 0.19, 0.16, 0.42, 0.28, 0.44],
    '2016': [1.27, 0.9, 0.43, 0.61, 0.78, 0.35, 0.52, 0.44, 0.08, 0.26, 0.18, 0.3],
    '2015': [1.24, 1.22, 1.32, 0.71, 0.74, 0.79, 0.62, 0.22, 0.54, 0.82, 1.01, 0.96]
  }
  
const poupanca = {
    '2018': [0.4273, 0.3994, 0.3994, 0.3855],
    '2017': [0.6858, 0.6709, 0.5304, 0.6527, 0.5000, 0.5768, 0.5539, 0.5626, 0.5512, 0.5000, 0.4690, 0.4273],
    '2016': [0.7261, 0.6327, 0.5962, 0.7179, 0.6311, 0.6541, 0.7053, 0.6629, 0.7558, 0.6583, 0.6609, 0.6435],
    '2015': [0.6058, 0.5882, 0.5169, 0.6302, 0.6079, 0.6159, 0.6822, 0.7317, 0.6876, 0.6930, 0.6799, 0.6303]
  }









function redimentoCompostoVariado(mesInicial, mesFinal) {


    let mesIni = mesInicial.split('/')
    let mesFin = mesFinal.split('/')
    console.log(mesIni, mesFin)
    for (i of mesIni){
    let mesInic = mesIni.i
    console.log('mês inicial: ' + mesInic)
    }
}

console.log(redimentoCompostoVariado('01/2015', '12/2017')) //=> 20161.722546560424
// console.log(redimentoCompostoVariado(poupanca, 0, 500, '01/2015', '12/2015')) //=> 6263.110235582166
// console.log(redimentoCompostoVariado(ipca, 0, 500, '01/2015', '12/2017')) //=> 19334.152800685235
// console.log(redimentoCompostoVariado(ipca, 0, 500, '01/2015', '12/2015')) //=> 6312.287539035425
