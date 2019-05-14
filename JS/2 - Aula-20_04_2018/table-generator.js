
function createTable(rows, cols, text = '') {
  let result = ''

  for (let row = 1; row <= rows; row++) {
    for (let col = 1; col <= cols; col++) {
      result += `${text}${row}.${col}`
      
      if (col == cols)
        result += '\n'
      else
        result += ' '
    }
  }

  return result
}

function createTableHTML(rows, cols, text = '') {
  let result = '<table>\n'

  for (let row = 1; row <= rows; row++) {
    result += '<tr>\n'
    let tds = []
    
    for (let col = 1; col <= cols; col++) {
      tds.push(`<td>${text}${row}.${col}</td>\n`)
    }
    result += tds.join('')
    result += '</tr>\n'
  }

  result += '</table>\n'
  return result
}

function createTableHTMLNEW(rows, cols, text = '') {
  let result = '<table>\n'

  for (let row = 1; row <= rows; row++) {
    result += '<tr>\n'
    
    for (let col = 1; col <= cols; col++) {
      result += `<td>${text}${row}.${col}</td>\n`
    }
    result += '</tr>\n'
  }

  result += '</table>\n'
  return result
}

//console.log(createTable(3, 4))
//console.log(createTableHTML(3, 4))
console.log(createTableHTMLNEW(3, 4))
