let hexa = document.querySelector('#hexadecimal')
let deci = document.querySelector('#decimal')
let octa = document.querySelector('#octal')
let bina = document.querySelector('#binary')

const buttonhex = document.querySelector('#converterHex')
const buttondec = document.querySelector('#converterDec')
const buttonoct = document.querySelector('#converterOct')
const buttonbin = document.querySelector('#converterBin')

buttonhex.addEventListener('click', function(event) {
    event.preventDefault()
    deci.value = parseInt(hexa.value, 16).toString(10)
    octa.value = parseInt(hexa.value, 16).toString(8)
    bina.value = parseInt(hexa.value, 16).toString(2)
})

buttondec.addEventListener('click', function(event) {
    event.preventDefault()
    hexa.value = parseInt(deci.value, 10).toString(16)
    octa.value = parseInt(deci.value, 10).toString(8)
    bina.value = parseInt(deci.value, 10).toString(2)
})

buttonoct.addEventListener('click', function(event) {
    event.preventDefault()
    hexa.value = parseInt(octa.value, 8).toString(16)
    deci.value = parseInt(octa.value, 8).toString(10)
    bina.value = parseInt(octa.value, 8).toString(2)
})

buttonbin.addEventListener('click', function(event) {
    event.preventDefault()
    deci.value = parseInt(bina.value, 2).toString(10)
    octa.value = parseInt(bina.value, 2).toString(8)
    hexa.value = parseInt(bina.value, 2).toString(16)
})