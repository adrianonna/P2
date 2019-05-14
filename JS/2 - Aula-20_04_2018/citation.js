function citation(name) {
  let result = ''
  
  let words = name.split(' ')
  
  let lastWord = words.pop()
  
  lastWord = lastWord.toUpperCase()
  
  words = words.join(' ')
  
  result = `${lastWord}; ${words}`
  
  return result
}


let nome = 'Thiago José Marques Moura'

console.log(citation(nome))




function compactCitation(name) {
  let result = ''
  let words = name.split(' ')
  let lastWord = words.pop()
  lastWord = lastWord.toUpperCase()

  words = words.map(word => `${word[0].toUpperCase()}.`)
  words = words.join(' ')
  result = `${lastWord}; ${words}`
  return result
}

//console.log(compactCitation(nome))
