const API_URL = "http://localhost:8000/api/add_to_cart.php"; // Endpoint correcto para agregar al carrito

let carrito = [];

// Función para agregar un producto al carrito
function agregarAlCarrito(productoId, cantidad) {
    const producto = carrito.find(p => p.id_prod === productoId);
    if (producto) {
        producto.cantidad += cantidad;
    } else {
        carrito.push({ id_prod: productoId, cantidad }); // Asegúrate de que sea id_prod
    }
    console.log(carrito);
}

// Función para eliminar un producto del carrito
function eliminarDelCarrito(productoId) {
    carrito = carrito.filter(p => p.id_prod !== productoId);
    console.log(carrito);
}

// Función para vaciar el carrito
function vaciarCarrito() {
    carrito = [];
    console.log(carrito);
}

// Función para calcular el total del carrito
function totalCarrito() {
    return carrito.reduce((total, producto) => total + (producto.cantidad * obtenerPrecio(producto.id_prod)), 0); // Asegúrate de que sea id_prod
}

// Simulación de obtención del precio del producto
function obtenerPrecio(productoId) {
    // Aquí puedes hacer una solicitud a la API para obtener el precio real del producto
    // Por ahora, vamos a simular un precio de 100 por producto
    return 100;
}

// Función para enviar el carrito a la API
async function enviarCarrito() {
    const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': obtenerCSRFToken() // Si es necesario
        },
        body: JSON.stringify({ items: carrito })
    });
    const data = await response.json();
    console.log(data);
}

// Simulación de obtención de CSRF Token
function obtenerCSRFToken() {
    // Aquí debes implementar la lógica para obtener el CSRF token si es necesario
    return "tu_csrf_token_aqui";
}
