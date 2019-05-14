const characters = [
    {
      comics: 'Marvel',
      height: 1.78,
      name: 'Spider-Man'
    },
    {
      comics: 'Marvel',
      height: 2.44,
      name: 'Hulk'
    },
    {
      comics: 'DC',
      height: 1.91,
      name: 'Superman'
    },  
    {
      comics: 'DC',
      height: 1.88,
      name: 'batman'
    }
  ]

let tam = characters.length;
let result = characters
//.map(c => c.height)
.reduce((acc,h) => acc + h.height,0);

console.log(result/tam)

//////////////////////////////
///////////////// Só DC
//////////////////////////////
let soDC = characters.filter(c => c.comics === 'DC');
console.log(soDC)
let tamDC = soDC.length;
let resultDC = soDC.map(c => c.height).reduce((acc,h) => acc + h,0);

console.log(resultDC/tamDC)