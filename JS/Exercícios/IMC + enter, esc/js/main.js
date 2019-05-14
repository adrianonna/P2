
const alturaElemento = document.querySelector('input[name=altura]')
const pesoKG = document.querySelector('input[name=peso]')
const imcElemento = document.querySelector('#imc')
const button = document.querySelector('button')


function calculadoraDeIMC() {
	const sexoElemento = document.querySelector('input[name=sexo]:checked')
    let sexo = sexoElemento.value
    let massa = pesoKG.value
    let altura = alturaElemento.value
    let imc = massa / (altura*altura)

	if (sexo == 'feminino'){
		if (imc < 20.7){
			imcElemento.value = 'Abaixo do Peso'
			imcElemento.setAttribute('class', 'border border-warning bg-warning text-white')
		}
		if (imc >= 20.7 && imc < 26.4){
			imcElemento.value = 'Peso Normal'
			imcElemento.setAttribute('class', 'border border-sucess bg-success text-white')
		}
		if (imc >= 26.4 && imc < 27.8){
			imcElemento.value = 'Marginalmente Acima do Peso'
			imcElemento.setAttribute('class', 'border border-warning bg-warning text-white')
		}
		if (imc >= 27.8 && imc <= 31.1){
			imcElemento.value = 'Acima do Peso Ideal'
			imcElemento.setAttribute('class', 'border border-warning bg-warning text-white')
		}
		if (imc > 31.1){
			imcElemento.value = 'Obeso'
			imcElemento.setAttribute('class', 'border border-danger bg-danger text-white')
		}
}

	if (sexo == 'masculino'){
		if (imc < 19.1){
			imcElemento.value = 'Abaixo do Peso'
			imcElemento.setAttribute('class', 'border border-warning bg-warning text-white')
		}
		if (imc >= 19.1 && imc < 25.8){
			imcElemento.value = 'Peso Normal'
			imcElemento.setAttribute('class', 'border border-sucess bg-success text-white')
		}
		if (imc >= 25.8 && imc < 27.3){
			imcElemento.value = 'Marginalmente Acima do Peso'
			imcElemento.setAttribute('class', 'border border-warning bg-warning text-white')
		}
		if (imc >= 27.3 && imc <= 32.3){
			imcElemento.value = 'Acima do Peso Ideal'
			imcElemento.setAttribute('class', 'border border-warning bg-warning text-white')
		}
		if (imc > 32.3){
			imcElemento.value = 'Obeso'
			imcElemento.setAttribute('class', 'border border-danger bg-danger text-white')
		}
	}
}

document.addEventListener('keyup', function(event) {
    if (event.key == 'Escape') {
        pesoKG.value = ''
        alturaElemento.value = ''
		imcElemento.value = ''
        altura.focus()
    } else if (event.key == 'Enter') {
        calculadoraDeIMC()
    }
  })

button.addEventListener('click', function() {
    calculadoraDeIMC()
  })


