from django.db import models

class Categoria(models.Model):
    nom_categoria = models.CharField(max_length=30, default="Desconocido")  # Añadir un valor por defecto

    def __str__(self):
        return self.nom_categoria

class Marca(models.Model):
    nom_marca = models.CharField(max_length=30, default="Desconocido")  # Añadir un valor por defecto

    def __str__(self):
        return self.nom_marca

class Producto(models.Model):
    sku = models.CharField(max_length=12, default="N/A")  # Añadir un valor por defecto
    nom_producto = models.CharField(max_length=30, default="Producto Desconocido")  # Añadir un valor por defecto
    modelo = models.CharField(max_length=20, null=True, blank=True, default="N/A")  # Añadir un valor por defecto
    descripcion = models.CharField(max_length=200, null=True, blank=True, default="Sin descripción")  # Añadir un valor por defecto
    precio = models.IntegerField(default=0)  # Cambiado a IntegerField y valor por defecto
    stock = models.IntegerField(default=0)  # Añadir un valor por defecto
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)  # Añadir un valor por defecto
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, default=1)  # Añadir un valor por defecto

    def __str__(self):
        return self.nom_producto

class Cliente(models.Model):
    nom_cli = models.CharField(max_length=20, default="Desconocido")  # Añadir un valor por defecto
    apaterno_cli = models.CharField(max_length=20, default="Desconocido")  # Añadir un valor por defecto
    amaterno_cli = models.CharField(max_length=20, null=True, blank=True, default="")  # Añadir un valor por defecto
    rut_cli = models.CharField(max_length=8, default="00000000")  # Añadir un valor por defecto
    dv_cli = models.CharField(max_length=1, default="0")  # Añadir un valor por defecto
    mail_cli = models.EmailField(max_length=30, null=True, blank=True, default="")  # Añadir un valor por defecto
    pass_cli = models.CharField(max_length=20, default="password")  # Añadir un valor por defecto
    numero_cli = models.CharField(max_length=9, null=True, blank=True, default="000000000")  # Añadir un valor por defecto
    direccion_cli = models.CharField(max_length=50, null=True, blank=True, default="Sin dirección")  # Añadir un valor por defecto

    def __str__(self):
        return f"{self.nom_cli} {self.apaterno_cli}"

class Sucursal(models.Model):
    nom_sucursal = models.CharField(max_length=30, default="Desconocido")  # Añadir un valor por defecto

    def __str__(self):
        return self.nom_sucursal

class Cargo(models.Model):
    nom_cargo = models.CharField(max_length=30, default="Desconocido")  # Añadir un valor por defecto

    def __str__(self):
        return self.nom_cargo

class Trabajador(models.Model):
    nom_trab = models.CharField(max_length=20, default="Desconocido")  # Añadir un valor por defecto
    apaterno_trab = models.CharField(max_length=20, default="Desconocido")  # Añadir un valor por defecto
    amaterno_trab = models.CharField(max_length=20, null=True, blank=True, default="")  # Añadir un valor por defecto
    rut_trab = models.CharField(max_length=8, default="00000000")  # Añadir un valor por defecto
    dv_trab = models.CharField(max_length=1, default="0")  # Añadir un valor por defecto
    mail_trab = models.EmailField(max_length=30, null=True, blank=True, default="")  # Añadir un valor por defecto
    pass_trab = models.CharField(max_length=20, default="password")  # Añadir un valor por defecto
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=True, blank=True, default=1)  # Añadir un valor por defecto
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, null=True, blank=True, default=1)  # Añadir un valor por defecto

    def __str__(self):
        return f"{self.nom_trab} {self.apaterno_trab}"

class Boleta(models.Model):
    fecha_boleta = models.DateField()
    cantidad = models.IntegerField(default=1)  # Añadir un valor por defecto
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Añadir un valor por defecto
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, default=1)  # Añadir un valor por defecto
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=1)  # Añadir un valor por defecto
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=1)  # Añadir un valor por defecto

    def __str__(self):
        return f"Boleta {self.id} - {self.fecha_boleta}"

class Carrito(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.cantidad * self.producto.precio
