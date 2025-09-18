"""
#Atributos privados
#Convencion de nombres para atrivutos privados
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self._titular = titular
        self._saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

cuenta = CuentaBancaria("Ana García", 1000)
# Esto funciona, pero no es recomendable
print(cuenta._saldo)  # Imprime: 1000

#Atributos realmente privados
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial, pin):
        self._titular = titular
        self._saldo = saldo_inicial
        self.__pin = pin  # Atributo "realmente" privado

    def validar_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado

cuenta = CuentaBancaria("Ana García", 1000, "1234")

# Esto generará un AttributeError
try:
    print(cuenta.__pin)
except AttributeError as e:
    print(f"Error: {e}")

# Esto funciona, pero requiere conocer el mecanismo interno
print(cuenta._CuentaBancaria__pin)  # Imprime: 1234

#Ejemplo practico validacion de datos
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        # Validamos el precio antes de asignarlo
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = precio

    # Los métodos para acceder y modificar vendrán en la siguiente sección

#Atributos privados vs protegidos
class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca      # Protegido (convención)
        self.__modelo = modelo   # Privado (name mangling)

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self._puertas = puertas

    def info(self):
        # Podemos acceder a _marca (protegido)
        print(f"Marca: {self._marca}")

        # Esto generará un AttributeError
        try:
            print(f"Modelo: {self.__modelo}")
        except AttributeError:
            print("No se puede acceder a __modelo desde la subclase")

#Getters y Setters
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Getter para nombre
    def get_nombre(self):
        return self._nombre

    # Setter para nombre
    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía")

    # Getter para edad
    def get_edad(self):
        return self._edad

    # Setter para edad
    def set_edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and 0 <= nueva_edad <= 120:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad debe ser un entero entre 0 y 120")

#Uso de getters y setters
# Crear una instancia
ana = Persona("Ana López", 29)

# Usar getters para acceder a los datos
print(ana.get_nombre())  # Ana López
print(ana.get_edad())    # 29

# Usar setters para modificar los datos
ana.set_nombre("Ana María López")
ana.set_edad(30)

# Verificar los cambios
print(ana.get_nombre())  # Ana María López
print(ana.get_edad())    # 30

# Intentar asignar un valor inválido
try:
    ana.set_edad(-5)
except ValueError as e:
    print(f"Error: {e}")  # Error: La edad debe ser un entero entre 0 y 120

#Ejemplo practico clase producto
class Producto:
    def __init__(self, nombre, precio, stock=0):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock
        self._descuento = 0

    # Getters
    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        # Aplicamos el descuento al devolver el precio
        return self._precio * (1 - self._descuento)

    def get_precio_base(self):
        # Devolvemos el precio sin descuento
        return self._precio

    def get_stock(self):
        return self._stock

    def get_descuento(self):
        return self._descuento

    # Setters
    def set_nombre(self, nuevo_nombre):
        if not isinstance(nuevo_nombre, str) or len(nuevo_nombre) == 0:
            raise ValueError("El nombre debe ser una cadena no vacía")
        self._nombre = nuevo_nombre

    def set_precio(self, nuevo_precio):
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio < 0:
            raise ValueError("El precio debe ser un número positivo")
        self._precio = nuevo_precio

    def set_stock(self, nuevo_stock):
        if not isinstance(nuevo_stock, int) or nuevo_stock < 0:
            raise ValueError("El stock debe ser un entero positivo")
        self._stock = nuevo_stock

    def set_descuento(self, nuevo_descuento):
        if not isinstance(nuevo_descuento, float) or not 0 <= nuevo_descuento <= 1:
            raise ValueError("El descuento debe ser un número entre 0 y 1")
        self._descuento = nuevo_descuento

#Ahora se puede usar la clase de forma segura
# Crear un producto
laptop = Producto("Laptop XPS", 1200.0, 10)

# Obtener información
print(f"Producto: {laptop.get_nombre()}")
print(f"Precio base: ${laptop.get_precio_base()}")
print(f"Stock disponible: {laptop.get_stock()} unidades")

# Aplicar un descuento del 15%
laptop.set_descuento(0.15)
print(f"Precio con descuento: ${laptop.get_precio()}")

# Actualizar el stock después de una venta
laptop.set_stock(laptop.get_stock() - 1)
print(f"Stock actualizado: {laptop.get_stock()} unidades")

# Intentar establecer un precio negativo
try:
    laptop.set_precio(-100)
except ValueError as e:
    print(f"Error: {e}")  # Error: El precio debe ser un número positivo

#Getters y setters en herencia
class Electrónico(Producto):
    def __init__(self, nombre, precio, stock, garantía_meses):
        super().__init__(nombre, precio, stock)
        self._garantía_meses = garantía_meses
        self._activado = False

    # Getters adicionales
    def get_garantía_meses(self):
        return self._garantía_meses

    def está_activado(self):
        return self._activado

    # Setters adicionales
    def set_garantía_meses(self, meses):
        if not isinstance(meses, int) or meses < 0:
            raise ValueError("Los meses de garantía deben ser un entero positivo")
        self._garantía_meses = meses

    def activar(self):
        self._activado = True

    def desactivar(self):
        self._activado = False

    # Sobrescribir el setter de precio para añadir lógica adicional
    def set_precio(self, nuevo_precio):
        # Llamamos al setter de la clase padre
        super().set_precio(nuevo_precio)
        # Lógica adicional específica para productos electrónicos
        if nuevo_precio > 1000:
            # Productos caros tienen garantía extendida automáticamente
            self._garantía_meses = max(self._garantía_meses, 24)

#Getters y setters vs acceso directo

class ConfiguraciónSimple:
    def __init__(self):
        self.modo_debug = False
        self.max_conexiones = 100
        self.tiempo_espera = 30


"""