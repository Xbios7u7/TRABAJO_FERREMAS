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

function anchoPage() {
    if (window.innerWidth > 850) {
        caja_trasera_register.style.display = "block";
        caja_trasera_login.style.display = "block";
        caja_trasera_register.style.opacity = "1";
        caja_trasera_login.style.opacity = "1";
        contenedor_login_register.style.left = "10px";
    } else {
        caja_trasera_register.style.display = "none";
        caja_trasera_login.style.display = "none";
        formulario_login.style.display = "block";
        formulario_register.style.display = "none";
        contenedor_login_register.style.left = "0px";
        mostrarBotonToggle();
    }
}

// Ejecutar anchoPage al cargar la página
anchoPage();

// Ajustar el diseño cuando se redimensiona la ventana
window.addEventListener('resize', anchoPage);

// Función para iniciar sesión
function iniciarSesion() {
    formulario_login.style.display = "block";
    formulario_register.style.display = "none";
    if (window.innerWidth > 850) {
        caja_trasera_register.style.opacity = "1";
        caja_trasera_login.style.opacity = "0";
        contenedor_login_register.style.left = "10px";
    } else {
        contenedor_login_register.style.left = "0px";
        mostrarBotonToggle();
    }
}

// Función para registrarse
function register() {
    formulario_register.style.display = "block";
    formulario_login.style.display = "none";
    if (window.innerWidth > 850) {
        caja_trasera_register.style.opacity = "0";
        caja_trasera_login.style.opacity = "1";
        contenedor_login_register.style.left = "410px";
    } else {
        contenedor_login_register.style.left = "0px";
        mostrarBotonToggle();
    }
}

// Función para mostrar el botón de toggle entre formularios
function mostrarBotonToggle() {
    let toggleButton = document.querySelector('.toggle-button');
    if (!toggleButton) {
        toggleButton = document.createElement('div');
        toggleButton.className = 'toggle-button';
        document.querySelector('.contenedor__login-register').appendChild(toggleButton);
    }
    if (formulario_login.style.display === "block") {
        toggleButton.innerText = "¿No tienes cuenta? Regístrate";
        toggleButton.onclick = register;
    } else {
        toggleButton.innerText = "¿Ya tienes cuenta? Inicia sesión";
        toggleButton.onclick = iniciarSesion;
    }
}

function verificarInicioSesion() {
    var usuarioIngresado = document.getElementById("input-usuario").value;
    var contraseñaIngresada = document.getElementById("input-contraseña").value;

    // Aquí deberías tener la lógica para verificar el usuario y la contraseña.
    // Por ahora, vamos a simular que las credenciales son incorrectas para mostrar el mensaje de error.
    var usuarioCorrecto = "usuarioCorrecto"; // Aquí deberías tener el usuario correcto almacenado
    var contraseñaCorrecta = "contraseñaCorrecta"; // Aquí deberías tener la contraseña correcta almacenada

    if (usuarioIngresado !== usuarioCorrecto || contraseñaIngresada !== contraseñaCorrecta) {
        mostrarErrorInicioSesionCliente(); // Mostrar mensaje de error del lado del cliente
        return false; // Prevenir el envío del formulario
    }

    return true; // Permitir el envío del formulario si las credenciales son correctas
}

// Función para mostrar el mensaje de error de inicio de sesión del lado del cliente
function mostrarErrorInicioSesionCliente() {
    var mensajeErrorCliente = document.getElementById("mensaje-error-contraseña-cliente");
    mensajeErrorCliente.style.display = "block";
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
