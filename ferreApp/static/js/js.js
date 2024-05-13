//Ejecutando funciones
document.getElementById("btn__iniciar-sesion").addEventListener("click", iniciarSesion);
document.getElementById("btn__registrarse").addEventListener("click", register);
window.addEventListener("resize", anchoPage);

//Declarando variables
var formulario_login = document.querySelector(".formulario__login");
var formulario_register = document.querySelector(".formulario__register");
var contenedor_login_register = document.querySelector(".contenedor__login-register");
var caja_trasera_login = document.querySelector(".caja__trasera-login");
var caja_trasera_register = document.querySelector(".caja__trasera-register");

    //FUNCIONES

function anchoPage(){

    if (window.innerWidth > 850){
        caja_trasera_register.style.display = "block";
        caja_trasera_login.style.display = "block";
    }else{
        caja_trasera_register.style.display = "block";
        caja_trasera_register.style.opacity = "1";
        caja_trasera_login.style.display = "none";
        formulario_login.style.display = "block";
        contenedor_login_register.style.left = "0px";
        formulario_register.style.display = "none";   
    }
}

anchoPage();


    function iniciarSesion(){
        if (window.innerWidth > 850){
            formulario_login.style.display = "block";
            contenedor_login_register.style.left = "10px";
            formulario_register.style.display = "none";
            caja_trasera_register.style.opacity = "1";
            caja_trasera_login.style.opacity = "0";
        }else{
            formulario_login.style.display = "block";
            contenedor_login_register.style.left = "0px";
            formulario_register.style.display = "none";
            caja_trasera_register.style.display = "block";
            caja_trasera_login.style.display = "none";
        }
    }

    function register(){
        if (window.innerWidth > 850){
            formulario_register.style.display = "block";
            contenedor_login_register.style.left = "410px";
            formulario_login.style.display = "none";
            caja_trasera_register.style.opacity = "0";
            caja_trasera_login.style.opacity = "1";
        }else{
            formulario_register.style.display = "block";
            contenedor_login_register.style.left = "0px";
            formulario_login.style.display = "none";
            caja_trasera_register.style.display = "none";
            caja_trasera_login.style.display = "block";
            caja_trasera_login.style.opacity = "1";
        }
}




function mostrarErrorContrasema() {
    // Obtener el elemento del DOM donde se mostrará el mensaje de error
    var mensajeError = document.getElementById("mensaje-error-contraseña");

    // Mostrar el mensaje de error
    mensajeError.style.display = "block";
}

// Ejemplo de cómo llamar a la función mostrarErrorContraseña cuando la contraseña sea incorrecta
// Suponiendo que tienes un botón o evento que verifica la contraseña
function verificarContraseña() {
    var contraseñaIngresada = document.getElementById("input-contraseña").value;
    var contraseñaCorrecta = "contraseñaCorrecta"; // Aquí deberías tener la contraseña correcta almacenada

    if (contraseñaIngresada !== contraseñaCorrecta) {
        console.log("Contraseña correcta ");
        // La contraseña es incorrecta, así que mostramos el mensaje de error
        mostrarErrorContraseña();
    } else {
        console.log("Contraseña incorrecta ");
        // La contraseña es correcta, puedes hacer algo aquí si lo necesitas
    }
}

function verDetallePedido(numeroPedido) {
    // Aquí va la lógica para mostrar el detalle del pedido con el número dado
    console.log('Detalles del pedido:', numeroPedido);
}
