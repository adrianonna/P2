let url= 'https://viacep.com.br/ws/58015430/json/';

const logradouro = document.querySelector('#logradouro')
const bairro = document.querySelector('#bairro')

let bairros = fetch(url)
    .then(res=>res.json())
    .then(json=> funcao(json))

    
    function funcao (x){
        logradouro.innerHTML = x.logradouro
        bairro.innerHTML = x.bairro
    }