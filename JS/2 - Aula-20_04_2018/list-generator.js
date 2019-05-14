
function createList(number, texto='Text') {
  let result = '<ul>\n'
  
  for (let cont = 1; cont <= number; cont++) {
    result += `<li>${texto} ${cont}</li>\n`
    //result += "<li>" + texto + " " + cont + "</li>\n"
  }
  result += '</ul>'
  
  return result
}

//console.log(createList(5))
console.log(createList(5, 'Item'))
