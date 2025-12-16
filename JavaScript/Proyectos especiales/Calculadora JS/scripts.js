let primerNumero=document.getElementById("primerVisor");
let segundoNumero=document.getElementById("segundoVisor");
let textoResultado=document.getElementById("tercerVisor");


function suma(x,y){
    return x+y;
}
function sumar(){
    let elementoSuma=suma(Number(primerNumero.value),Number(segundoNumero.value));
    textoResultado.textContent=elementoSuma;
}
function resta(x,y){
    return x-y;
}
function restar(){
    let elementoResta=resta(Number(primerNumero.value),Number(segundoNumero.value));
    textoResultado.textContent=elementoResta;
}
function multiplicacion(x,y){
    return x*y;
}
function multiplicar(){
    let elementoMultiplicacion=multiplicacion(Number(primerNumero.value),Number(segundoNumero.value));
    textoResultado.textContent=elementoMultiplicacion;
}
function division(x,y){
    return x/y;
}
function dividir(){
    let elementoDivision=division(Number(primerNumero.value),Number(segundoNumero.value));
    textoResultado.textContent=elementoDivision;
}
function potencia(x,y){
    return Math.pow(x,y);
}
function potenciar(){
    let elementoPotencia=potencia(Number(primerNumero.value),Number(segundoNumero.value));
    textoResultado.textContent=elementoPotencia;
}
function sacar_raiz(x){
    return Math.sqrt(x);
}
function raiz(){
    let elementoRaiz=sacar_raiz(Number(primerNumero.value));
    textoResultado.textContent=elementoRaiz;
}
function sacar_absoluto(x){
    return Math.abs(x);
}
function absoluto(){
    let elementoAbsoluto=sacar_absoluto(Number(primerNumero.value));
    textoResultado.textContent=elementoAbsoluto;
}
function sacar_aleatorio(x,y){
    return Math.floor(Math.random()*(x-y)+y);
}
function aleatorio(){
    let elementoAleatorio=sacar_aleatorio(Number(primerNumero.value),Number(segundoNumero.value));
    textoResultado.textContent=elementoAleatorio;
}
function redondo(x){
    return Math.round(x);
}
function redondear(){
    let elementoRedondear=redondo(Number(primerNumero.value));
    textoResultado.textContent=elementoRedondear;
}
function redondo_abajo(x){
    return Math.floor(x);
}
function redondear_piso(){
    let elementoRedondearPiso=redondo_abajo(Number(primerNumero.value));
    textoResultado.textContent=elementoRedondearPiso;
}
function redondo_arriba(x){
    return Math.ceil(x);
}
function redondear_techo(){
    let elementoRedondearTecho=redondo_arriba(Number(primerNumero.value));
    textoResultado.textContent=elementoRedondearTecho;
}