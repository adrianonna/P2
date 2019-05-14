const input = document.querySelector('input')
const button = document.querySelector('button')
const ul = document.querySelector('.list')

button.addEventListener('click', function() {
    for (let i =1; i <= input.value; i++){
        let lis = `<li>Item ${i}</li>`
        ul.insertAdjacentHTML('beforeend', lis)
    }
})
