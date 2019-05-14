
function hamming(dna1, dna2){
  let diff = 0
  for (let char = 0; char < dna1.length; char++) {
    if (dna1[char] != dna2[char]) diff++
  }
  return diff
}

let dna1 = 'GGACGGATTCTG'
let dna2 = 'AGGACGGATTCT'

console.log(hamming(dna1, dna2))
