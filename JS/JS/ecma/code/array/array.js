
function min(array) {
 let menor = array[0]
 for(const value of array){
   if(value < menor)
    menor = value
 }
 return menor
}

function max(array) {
  let maior = array[0]
  for(const value of array){
    if(value > maior)
     maior = value
  }
  return maior
}

function range(length, last, step) {
  let array = []
  for(i = 0; i < last; i=i+step){
    array.push
  }
  
  console.log(range(0, 30, 5))
}

function zip(...arrays) {
  // TODO
}

function uniq(array) {
  // TODO
}

export { min, max, range, zip, uniq }
