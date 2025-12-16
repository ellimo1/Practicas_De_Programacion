let contador=0;

const valorContador=document.getElementById("valorContador");
const botonAumentar=document.getElementById("ascender");
const botonDisminuir=document.getElementById("descender");

function actualizarContador(valor){
    valorContador.textContent=valor;
}
function aumentar(){
    contador++;
    actualizarContador(contador);
}
function disminuir(){
    contador--;
    actualizarContador(contador);
}
botonAumentar.addEventListener("click",aumentar);
botonDisminuir.addEventListener("click",disminuir);