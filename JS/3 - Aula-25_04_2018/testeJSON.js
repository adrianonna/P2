////////////////
// Post JSON
////////////////
let post = {
    title: 'Lorem ipsum dolor',
    text: 'Nunc accumsan in ipsum a mattis...'
  }
  
console.log(post)          //=> { title: 'Lorem ipsum dolor', text: 'Nunc accumsan in ipsum a mattis...' }
console.log(post.title)    //=> 'Lorem ipsum dolor'
console.log(post['title']) //=> 'Lorem ipsum dolor'
console.log(post.text)     //=> 'Nunc accumsan in ipsum a mattis...'
console.log(typeof post)   //=> object

////////////////
// Post Object
////////////////
let newPost = new Object()
newPost.title = 'Lorem ipsum dolor'
newPost.text = 'Nunc accumsan in ipsum a mattis...'

console.log(newPost)        //=> { title: 'Lorem ipsum dolor', text: 'Nunc accumsan in ipsum a mattis...' }
console.log(typeof newPost) //=> object

////////////////
// Object.keys(obj) – retorna um array de strings. Cada elemento é uma chave
// Object.values(obj) – retorna um array de valores
// Object.entries(obj) – retorna um array de [chave,valor]
////////////////
post = {
  title: 'Lorem ipsum dolor',
  text: 'Nunc accumsan in ipsum a mattis...'
}

for (let i in post)
  console.log(post[i])

for (let i of Object.keys(post))
  console.log(post[i])

for(let value of Object.values(post))
  console.log(value)

for(let [key,value] of Object.entries(post))
    console.log(value)

////////////////
// Exemplo mais complexo!
////////////////

let people = [
  {
    name: 'Mike Smith',
    family: {
      mother: 'Jane Smith',
      father: 'Harry Smith',
      sister: 'Samantha Smith'
    },
    age: 35
  },
  {
    name: 'Tom Jones',
    family: {
      mother: 'Norah Jones',
      father: 'Richard Jones',
      brother: 'Howard Jones'
    },
    age: 25
  }
]

for (let {name: n, family: { father: f } } of people) {
  console.log('Name: ' + n + ', Father: ' + f)
}


