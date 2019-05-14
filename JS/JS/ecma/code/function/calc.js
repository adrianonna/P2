/**
 * operator: '+', '-', '*', '/'
 */
function calc(operand1, operand2, operator){
  return eval(operand1 + operator + operand2)
}

export {calc}
