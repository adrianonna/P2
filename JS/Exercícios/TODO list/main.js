const textarea = document.querySelector('#task')
const button = document.querySelector('button')
const ultop = document.querySelector('#top-tasks')
const ulnormal = document.querySelector('#tasks')
let priority = document.querySelector('input')

button.addEventListener('click', function(event) {
    if (priority.checked == true){
        ultop.insertAdjacentHTML('afterbegin', `<li> ${textarea.value}</li>`)
    }
    else{
        ulnormal.insertAdjacentHTML('afterbegin', `<li>${textarea.value}</li>`)
    }
  })
