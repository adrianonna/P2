
const alturaElemento = document.querySelector('input[name=altura]')
const pesoKG = document.querySelector('input[name=peso]')
const imcElemento = document.querySelector('#imc')

function calculadoraDeIMC() {
	const sexoElemento = document.querySelector('input[name=sexo]:checked')
	let massa = pesoKG.value
	let sexo = sexoElemento.value
	let altura = alturaElemento.value
	let imc = massa / (altura*altura)

	if (sexo == 'feminino'){
		if (imc < 20.7){
			imcElemento.value = 'Abaixo do Peso'
		}
		if (imc >= 20.7 && imc < 26.4){
			imcElemento.value = 'Peso Normal'
		}
		if (imc >= 26.4 && imc < 27.8){
			imcElemento.value = 'Marginalmente Acima do Peso'
		}
		if (imc >= 27.8 && imc <= 31.1){
			imcElemento.value = 'Acima do Peso Ideal'
		}
		if (imc > 31.1){
			imcElemento.value = 'Obeso'
		}
}

	if (sexo == 'masculino'){
		if (imc < 19.1){
			imcElemento.value = 'Abaixo do Peso'
		}
		if (imc >= 19.1 && imc < 25.8){
			imcElemento.value = 'Peso Normal'
		}
		if (imc >= 25.8 && imc < 27.3){
			imcElemento.value = 'Marginalmente Acima do Peso'
		}
		if (imc >= 27.3 && imc <= 32.3){
			imcElemento.value = 'Acima do Peso Ideal'
		}
		if (imc > 32.3){
			imcElemento.value = 'Obeso'
		}
	}
}








