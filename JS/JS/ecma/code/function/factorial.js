function factorial(number){
   if (number == 0){
    return 0
  }


  return number + factorial(number - 1) 

  return (number === 0) ? 0 : number + factorial(number - 1);
}

export { factorial }
