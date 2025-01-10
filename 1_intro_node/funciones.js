// Arrow function (Funcion tipo flecha)
// Funcion anonima
const sumar = (numero1, numero2) => {
    const resultado = numero1 + numero2
    return resultado
}

// Funcion tradicional
function restar(numero1, numero2) {
    const resultado = numero1 - numero2
    return resultado
}

// Adicional a ello, si la funcion es de una sola linea, retornara el resultado
const multiplicar = (numero1, numero2) => numero1 * numero2

// Segun commonJS, para realizar una exportacion se realiza asi
module.exports = {
    sumar: sumar,
    restar,
    multiplicar,
}

