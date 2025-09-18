from datetime import datetime
from abc import ABC, abstractmethod


class Equipo:
    """Clase base que representa un equipo en el sistema de préstamos"""
    
    def __init__(self, nombre, tipo_equipo):
        """
        Constructor de la clase Equipo
        
        Args:
            nombre (str): Nombre del equipo
            tipo_equipo (str): Tipo de equipo (computadora, tablet, etc.)
        """
        self._nombre = nombre
        self._tipo_equipo = tipo_equipo
        self._disponible = True
        self._historial_prestamos = []
    
    @property
    def nombre(self):
        """Propiedad de solo lectura para el nombre del equipo"""
        return self._nombre
    
    @property
    def tipo_equipo(self):
        """Propiedad de solo lectura para el tipo de equipo"""
        return self._tipo_equipo
    
    @property
    def disponible(self):
        """Propiedad para verificar disponibilidad"""
        return self._disponible
    
    @property
    def historial_prestamos(self):
        """Propiedad de solo lectura para el historial de préstamos"""
        return self._historial_prestamos.copy()  # Retorna copia para proteger datos
    
    def prestar(self, usuario):
        """
        Presta el equipo a un usuario
        
        Args:
            usuario (str): Nombre del usuario
            
        Returns:
            bool: True si el préstamo fue exitoso, False en caso contrario
        """
        if not self._disponible:
            return False
        
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        prestamo = (usuario, fecha_actual)
        self._historial_prestamos.append(prestamo)
        self._disponible = False
        return True
    
    def devolver(self):
        """
        Devuelve el equipo al sistema
        
        Returns:
            bool: True si la devolución fue exitosa, False en caso contrario
        """
        if self._disponible:
            return False
        
        self._disponible = True
        return True
    
    def __str__(self):
        """Representación en cadena del equipo"""
        estado = "Disponible" if self._disponible else "Prestado"
        return f"{self._nombre} ({self._tipo_equipo}) - {estado}"


class EquipoComputo(Equipo):
    """Clase específica para equipos de cómputo"""
    
    def __init__(self, nombre, sistema_operativo="Windows", ram="8GB"):
        """
        Constructor para equipo de cómputo
        
        Args:
            nombre (str): Nombre del equipo
            sistema_operativo (str): Sistema operativo instalado
            ram (str): Cantidad de RAM
        """
        super().__init__(nombre, "Computadora")
        self._sistema_operativo = sistema_operativo
        self._ram = ram
    
    @property
    def sistema_operativo(self):
        """Propiedad para el sistema operativo"""
        return self._sistema_operativo
    
    @property
    def ram(self):
        """Propiedad para la RAM"""
        return self._ram
    
    def __str__(self):
        """Representación específica para equipos de cómputo"""
        estado = "Disponible" if self._disponible else "Prestado"
        return f"{self._nombre} (Computadora - {self._sistema_operativo}, {self._ram}) - {estado}"


class Tablet(Equipo):
    """Clase específica para tablets"""
    
    def __init__(self, nombre, pulgadas="10", bateria="8000mAh"):
        """
        Constructor para tablet
        
        Args:
            nombre (str): Nombre de la tablet
            pulgadas (str): Tamaño de pantalla en pulgadas
            bateria (str): Capacidad de batería
        """
        super().__init__(nombre, "Tablet")
        self._pulgadas = pulgadas
        self._bateria = bateria
    
    @property
    def pulgadas(self):
        """Propiedad para el tamaño de pantalla"""
        return self._pulgadas
    
    @property
    def bateria(self):
        """Propiedad para la batería"""
        return self._bateria
    
    def __str__(self):
        """Representación específica para tablets"""
        estado = "Disponible" if self._disponible else "Prestado"
        return f"{self._nombre} (Tablet - {self._pulgadas}\", {self._bateria}) - {estado}"


class Usuario:
    """Clase que representa un usuario del sistema"""
    
    def __init__(self, nombre, email, tipo_usuario="Estudiante"):
        """
        Constructor de la clase Usuario
        
        Args:
            nombre (str): Nombre del usuario
            email (str): Email del usuario
            tipo_usuario (str): Tipo de usuario (Estudiante, Profesor, Admin)
        """
        self._nombre = nombre
        self._email = email
        self._tipo_usuario = tipo_usuario
        self._equipos_prestados = []
    
    @property
    def nombre(self):
        """Propiedad de solo lectura para el nombre"""
        return self._nombre
    
    @property
    def email(self):
        """Propiedad de solo lectura para el email"""
        return self._email
    
    @property
    def tipo_usuario(self):
        """Propiedad de solo lectura para el tipo de usuario"""
        return self._tipo_usuario
    
    @property
    def equipos_prestados(self):
        """Propiedad de solo lectura para equipos prestados"""
        return self._equipos_prestados.copy()
    
    def agregar_equipo_prestado(self, equipo):
        """Agrega un equipo a la lista de prestados del usuario"""
        if equipo not in self._equipos_prestados:
            self._equipos_prestados.append(equipo)
    
    def remover_equipo_prestado(self, equipo):
        """Remueve un equipo de la lista de prestados del usuario"""
        if equipo in self._equipos_prestados:
            self._equipos_prestados.remove(equipo)
    
    def __str__(self):
        """Representación en cadena del usuario"""
        return f"{self._nombre} ({self._tipo_usuario}) - {self._email}"


class SistemaPrestamos:
    """Clase principal que gestiona el sistema de préstamos"""
    
    def __init__(self):
        """Constructor del sistema de préstamos"""
        self._equipos = {}  # Diccionario: nombre -> objeto Equipo
        self._usuarios = {}  # Diccionario: nombre -> objeto Usuario
        self._inicializar_datos_prueba()
    
    def _inicializar_datos_prueba(self):
        """Inicializa el sistema con algunos datos de prueba"""
        # Agregar equipos de prueba
        self.agregar_equipo(EquipoComputo("Laptop-001", "Windows 11", "16GB"))
        self.agregar_equipo(EquipoComputo("Laptop-002", "macOS", "8GB"))
        self.agregar_equipo(Tablet("iPad-001", "12", "10000mAh"))
        self.agregar_equipo(Tablet("Samsung-Tab-001", "11", "8000mAh"))
        
        # Agregar usuarios de prueba
        self.agregar_usuario(Usuario("Juan Pérez", "juan@email.com", "Estudiante"))
        self.agregar_usuario(Usuario("María García", "maria@email.com", "Profesor"))
    
    def agregar_equipo(self, equipo):
        """
        Agrega un nuevo equipo al sistema
        
        Args:
            equipo (Equipo): Objeto equipo a agregar
            
        Returns:
            bool: True si se agregó exitosamente, False si ya existe
        """
        if equipo.nombre in self._equipos:
            return False
        
        self._equipos[equipo.nombre] = equipo
        return True
    
    def agregar_usuario(self, usuario):
        """
        Agrega un nuevo usuario al sistema
        
        Args:
            usuario (Usuario): Objeto usuario a agregar
            
        Returns:
            bool: True si se agregó exitosamente, False si ya existe
        """
        if usuario.nombre in self._usuarios:
            return False
        
        self._usuarios[usuario.nombre] = usuario
        return True
    
    def mostrar_equipos(self):
        """Muestra todos los equipos registrados en el sistema"""
        if not self._equipos:
            print("No hay equipos registrados en el sistema.")
            return
        
        print("\n=== INVENTARIO DE EQUIPOS ===")
        for equipo in self._equipos.values():
            print(f"  • {equipo}")
    
    def mostrar_equipos_disponibles(self):
        """Muestra solo los equipos disponibles"""
        equipos_disponibles = [equipo for equipo in self._equipos.values() if equipo.disponible]
        
        if not equipos_disponibles:
            print("No hay equipos disponibles actualmente.")
            return
        
        print("\n=== EQUIPOS DISPONIBLES ===")
        for equipo in equipos_disponibles:
            print(f"  • {equipo}")
    
    def registrar_prestamo(self, nombre_equipo, nombre_usuario):
        """
        Registra un nuevo préstamo
        
        Args:
            nombre_equipo (str): Nombre del equipo a prestar
            nombre_usuario (str): Nombre del usuario que hace el préstamo
            
        Returns:
            tuple: (bool, str) - (éxito, mensaje)
        """
        # Verificar que el equipo existe
        if nombre_equipo not in self._equipos:
            return False, f"El equipo '{nombre_equipo}' no existe en el sistema."
        
        equipo = self._equipos[nombre_equipo]
        
        # Verificar que el equipo esté disponible
        if not equipo.disponible:
            return False, f"El equipo '{nombre_equipo}' ya está prestado."
        
        # Verificar que el usuario existe (si no, crearlo)
        if nombre_usuario not in self._usuarios:
            nuevo_usuario = Usuario(nombre_usuario, f"{nombre_usuario.lower().replace(' ', '')}@email.com")
            self.agregar_usuario(nuevo_usuario)
        
        usuario = self._usuarios[nombre_usuario]
        
        # Realizar el préstamo
        if equipo.prestar(nombre_usuario):
            usuario.agregar_equipo_prestado(equipo.nombre)
            return True, f"Préstamo registrado exitosamente. {equipo.nombre} prestado a {nombre_usuario}."
        
        return False, "Error al registrar el préstamo."
    
    def devolver_equipo(self, nombre_equipo):
        """
        Procesa la devolución de un equipo
        
        Args:
            nombre_equipo (str): Nombre del equipo a devolver
            
        Returns:
            tuple: (bool, str) - (éxito, mensaje)
        """
        # Verificar que el equipo existe
        if nombre_equipo not in self._equipos:
            return False, f"El equipo '{nombre_equipo}' no existe en el sistema."
        
        equipo = self._equipos[nombre_equipo]
        
        # Verificar que el equipo esté prestado
        if equipo.disponible:
            return False, f"El equipo '{nombre_equipo}' ya está disponible."
        
        # Buscar el usuario que tiene el equipo
        usuario_con_equipo = None
        for usuario in self._usuarios.values():
            if nombre_equipo in usuario.equipos_prestados:
                usuario_con_equipo = usuario
                break
        
        # Realizar la devolución
        if equipo.devolver():
            if usuario_con_equipo:
                usuario_con_equipo.remover_equipo_prestado(nombre_equipo)
            return True, f"Equipo '{nombre_equipo}' devuelto exitosamente."
        
        return False, "Error al devolver el equipo."
    
    def ver_historial_completo(self):
        """Muestra el historial completo de préstamos"""
        print("\n=== HISTORIAL DE PRÉSTAMOS ===")
        
        for nombre_equipo, equipo in self._equipos.items():
            print(f"\n📱 {equipo}")
            
            if not equipo.historial_prestamos:
                print("   Sin préstamos registrados.")
            else:
                print("   Historial de préstamos:")
                for i, (usuario, fecha) in enumerate(equipo.historial_prestamos, 1):
                    print(f"   {i}. {usuario} - {fecha}")
    
    def ver_historial_equipo(self, nombre_equipo):
        """
        Muestra el historial de un equipo específico
        
        Args:
            nombre_equipo (str): Nombre del equipo
        """
        if nombre_equipo not in self._equipos:
            print(f"El equipo '{nombre_equipo}' no existe en el sistema.")
            return
        
        equipo = self._equipos[nombre_equipo]
        print(f"\n=== HISTORIAL DE {nombre_equipo.upper()} ===")
        
        if not equipo.historial_prestamos:
            print("Sin préstamos registrados.")
        else:
            for i, (usuario, fecha) in enumerate(equipo.historial_prestamos, 1):
                print(f"{i}. {usuario} - {fecha}")
    
    def mostrar_usuarios(self):
        """Muestra todos los usuarios registrados"""
        if not self._usuarios:
            print("No hay usuarios registrados.")
            return
        
        print("\n=== USUARIOS REGISTRADOS ===")
        for usuario in self._usuarios.values():
            print(f"  • {usuario}")
            if usuario.equipos_prestados:
                print(f"    Equipos prestados: {', '.join(usuario.equipos_prestados)}")
    
    def obtener_estadisticas(self):
        """Muestra estadísticas del sistema"""
        total_equipos = len(self._equipos)
        equipos_disponibles = sum(1 for equipo in self._equipos.values() if equipo.disponible)
        equipos_prestados = total_equipos - equipos_disponibles
        total_usuarios = len(self._usuarios)
        
        print(f"\n=== ESTADÍSTICAS DEL SISTEMA ===")
        print(f"Total de equipos: {total_equipos}")
        print(f"Equipos disponibles: {equipos_disponibles}")
        print(f"Equipos prestados: {equipos_prestados}")
        print(f"Total de usuarios: {total_usuarios}")
        
        # Contar préstamos totales
        total_prestamos = sum(len(equipo.historial_prestamos) for equipo in self._equipos.values())
        print(f"Total de préstamos realizados: {total_prestamos}")


class MenuSistema:
    """Clase que maneja la interfaz de usuario del sistema"""
    
    def __init__(self):
        """Constructor del menú"""
        self.sistema = SistemaPrestamos()
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal del sistema"""
        print("\n" + "="*50)
        print("   SISTEMA DE PRÉSTAMOS DE EQUIPOS")
        print("="*50)
        print("1. Ver todos los equipos")
        print("2. Ver equipos disponibles")
        print("3. Registrar préstamo")
        print("4. Devolver equipo")
        print("5. Ver historial completo")
        print("6. Ver historial de equipo específico")
        print("7. Agregar nuevo equipo")
        print("8. Ver usuarios")
        print("9. Ver estadísticas")
        print("0. Salir del programa")
        print("="*50)
    
    def solicitar_opcion(self):
        """Solicita al usuario que seleccione una opción"""
        try:
            opcion = int(input("Seleccione una opción (0-9): "))
            return opcion
        except ValueError:
            print("❌ Por favor, ingrese un número válido.")
            return -1
    
    def registrar_prestamo_interactivo(self):
        """Interfaz interactiva para registrar un préstamo"""
        print("\n=== REGISTRAR PRÉSTAMO ===")
        
        # Mostrar equipos disponibles
        self.sistema.mostrar_equipos_disponibles()
        
        if not any(equipo.disponible for equipo in self.sistema._equipos.values()):
            return
        
        nombre_equipo = input("\nIngrese el nombre exacto del equipo: ").strip()
        nombre_usuario = input("Ingrese el nombre del usuario: ").strip()
        
        if not nombre_equipo or not nombre_usuario:
            print("❌ Debe ingresar tanto el nombre del equipo como del usuario.")
            return
        
        exito, mensaje = self.sistema.registrar_prestamo(nombre_equipo, nombre_usuario)
        
        if exito:
            print(f"✅ {mensaje}")
        else:
            print(f"❌ {mensaje}")
    
    def devolver_equipo_interactivo(self):
        """Interfaz interactiva para devolver un equipo"""
        print("\n=== DEVOLVER EQUIPO ===")
        
        # Mostrar equipos prestados
        equipos_prestados = [equipo for equipo in self.sistema._equipos.values() if not equipo.disponible]
        
        if not equipos_prestados:
            print("No hay equipos prestados actualmente.")
            return
        
        print("Equipos actualmente prestados:")
        for equipo in equipos_prestados:
            print(f"  • {equipo}")
        
        nombre_equipo = input("\nIngrese el nombre exacto del equipo a devolver: ").strip()
        
        if not nombre_equipo:
            print("❌ Debe ingresar el nombre del equipo.")
            return
        
        exito, mensaje = self.sistema.devolver_equipo(nombre_equipo)
        
        if exito:
            print(f"✅ {mensaje}")
        else:
            print(f"❌ {mensaje}")
    
    def agregar_equipo_interactivo(self):
        """Interfaz interactiva para agregar un nuevo equipo"""
        print("\n=== AGREGAR NUEVO EQUIPO ===")
        print("Tipos de equipo disponibles:")
        print("1. Computadora")
        print("2. Tablet")
        
        try:
            tipo = int(input("Seleccione el tipo de equipo (1-2): "))
        except ValueError:
            print("❌ Opción inválida.")
            return
        
        nombre = input("Ingrese el nombre del equipo: ").strip()
        
        if not nombre:
            print("❌ El nombre del equipo no puede estar vacío.")
            return
        
        if tipo == 1:  # Computadora
            so = input("Sistema operativo (Windows): ").strip() or "Windows"
            ram = input("RAM (8GB): ").strip() or "8GB"
            equipo = EquipoComputo(nombre, so, ram)
        elif tipo == 2:  # Tablet
            pulgadas = input("Pulgadas (10): ").strip() or "10"
            bateria = input("Batería (8000mAh): ").strip() or "8000mAh"
            equipo = Tablet(nombre, pulgadas, bateria)
        else:
            print("❌ Tipo de equipo inválido.")
            return
        
        if self.sistema.agregar_equipo(equipo):
            print(f"✅ Equipo '{nombre}' agregado exitosamente.")
        else:
            print(f"❌ El equipo '{nombre}' ya existe en el sistema.")
    
    def ver_historial_especifico(self):
        """Ver historial de un equipo específico"""
        print("\n=== HISTORIAL DE EQUIPO ESPECÍFICO ===")
        self.sistema.mostrar_equipos()
        
        nombre_equipo = input("\nIngrese el nombre del equipo: ").strip()
        if nombre_equipo:
            self.sistema.ver_historial_equipo(nombre_equipo)
    
    def ejecutar(self):
        """Ejecuta el menú principal del sistema"""
        print("¡Bienvenido al Sistema de Préstamos de Equipos!")
        
        while True:
            self.mostrar_menu_principal()
            opcion = self.solicitar_opcion()
            
            if opcion == 0:
                print("\n¡Gracias por usar el Sistema de Préstamos de Equipos!")
                break
            elif opcion == 1:
                self.sistema.mostrar_equipos()
            elif opcion == 2:
                self.sistema.mostrar_equipos_disponibles()
            elif opcion == 3:
                self.registrar_prestamo_interactivo()
            elif opcion == 4:
                self.devolver_equipo_interactivo()
            elif opcion == 5:
                self.sistema.ver_historial_completo()
            elif opcion == 6:
                self.ver_historial_especifico()
            elif opcion == 7:
                self.agregar_equipo_interactivo()
            elif opcion == 8:
                self.sistema.mostrar_usuarios()
            elif opcion == 9:
                self.sistema.obtener_estadisticas()
            else:
                print("❌ Opción inválida. Por favor, seleccione una opción del 0 al 9.")
            
            input("\nPresione Enter para continuar...")


# Función principal para ejecutar el programa
def main():
    """Función principal que inicia el sistema"""
    menu = MenuSistema()
    menu.ejecutar()


if __name__ == "__main__":
    main()