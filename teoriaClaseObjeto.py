"""
#Clases: Los planos
class Coche:
    # Aquí definiremos los atributos y métodos
    pass
    
#Objetos: Las instancias concretas
# Creamos dos objetos de tipo Coche
mi_coche = Coche()
coche_de_amigo = Coche()

#Ejemplo conceptual
class Libro:
    # Aquí definiremos atributos como título, autor, páginas
    # Y métodos como abrir(), leer(), cerrar()
    pass

# Creamos objetos (instancias) de la clase Libro
libro_python = Libro()  # Un libro específico sobre Python
novela_fantasia = Libro()  # Una novela de fantasía específica

#Clase constructor
class Persona:
    # Aquí irá el código de la clase
    pass

    
#El metodo constructor: __init__
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

#El parametro: self
# Creamos un objeto Persona
ana = Persona("Ana García", 28)

# Python internamente hace algo equivalente a:
# Persona.__init__(ana, "Ana García", 28)

#Creacion de objetos:
# Creamos dos objetos Persona
ana = Persona("Ana García", 28)
juan = Persona("Juan López", 35)

# Accedemos a sus atributos
print(ana.nombre)  # Imprime: Ana García
print(juan.edad)   # Imprime: 35

#Valores predeterminados en el constructor
class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

# Creamos productos con y sin especificar el stock
laptop = Producto("Laptop XPS", 1200)  # stock será 0
teclado = Producto("Teclado mecánico", 80, 15)  # stock será 15

print(laptop.stock)  # Imprime: 0
print(teclado.stock)  # Imprime: 15

#Inicializacion de atributos con calculos
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.area = ancho * alto  # Calculamos y almacenamos el área
        self.perimetro = 2 * (ancho + alto)  # Calculamos y almacenamos el perímetro

# Creamos un rectángulo
rect = Rectangulo(5, 3)
print(rect.area)      # Imprime: 15
print(rect.perimetro) # Imprime: 16

#Atributos con validacion
class Cuenta:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular

        # Validamos que el saldo inicial no sea negativo
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")

        self.saldo = saldo_inicial

# Esto funcionará
cuenta_ana = Cuenta("Ana García", 1000)

# Esto lanzará un ValueError
try:
    cuenta_problematica = Cuenta("Juan López", -500)
except ValueError as e:
    print(f"Error: {e}")  # Imprime: Error: El saldo inicial no puede ser negativo

#Ejemplo práctico: Modelando una biblioteca
class Libro:
    def __init__(self, titulo, autor, paginas, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.isbn = isbn
        self.disponible = disponible
        self.pagina_actual = 0  # Inicializamos en la página 0 (cerrado)

# Creamos algunos libros
libro1 = Libro("Python Crash Course", "Eric Matthes", 544, "9781593279288")
libro2 = Libro("Clean Code", "Robert C. Martin", 464, "9780132350884", False)

# Verificamos si están disponibles
print(f"{libro1.titulo} está {'disponible' if libro1.disponible else 'prestado'}")
print(f"{libro2.titulo} está {'disponible' if libro2.disponible else 'prestado'}")

#Constructores alternativos con métodos de clase
"""
class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    @classmethod
    def desde_texto(cls, texto):
        """Constructor alternativo que crea una Fecha desde un texto con formato DD-MM-AAAA"""
        dia, mes, año = map(int, texto.split('-'))
        return cls(dia, mes, año)

    @classmethod
    def hoy(cls):
        """Constructor alternativo que crea una Fecha con la fecha actual"""
        import datetime
        fecha_actual = datetime.date.today()
        return cls(fecha_actual.day, fecha_actual.month, fecha_actual.year)

# Diferentes formas de crear objetos Fecha
fecha1 = Fecha(15, 3, 2023)  # Constructor normal
fecha2 = Fecha.desde_texto("25-12-2023")  # Constructor alternativo
fecha3 = Fecha.hoy()  # Constructor alternativo que usa la fecha actual

print(f"{fecha1.dia}/{fecha1.mes}/{fecha1.año}")  # Imprime: 15/3/2023
print(f"{fecha2.dia}/{fecha2.mes}/{fecha2.año}")  # Imprime: 25/12/2023
"""
"""