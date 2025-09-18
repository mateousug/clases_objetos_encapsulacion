class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        """
        Constructor de la clase CuentaBancaria
        
        Args:
            titular (str): Nombre del titular de la cuenta
            saldo_inicial (float): Saldo inicial de la cuenta (por defecto 0)
        
        Raises:
            ValueError: Si el saldo inicial es negativo
        """
        self._titular = titular
        if saldo_inicial < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = float(saldo_inicial)
    
    @property
    def titular(self):
        """
        Propiedad de solo lectura para obtener el titular
        
        Returns:
            str: Nombre del titular de la cuenta
        """
        return self._titular
    
    @property
    def saldo(self):
        """
        Propiedad para obtener el saldo actual
        
        Returns:
            float: Saldo actual de la cuenta
        """
        return self._saldo
    
    @saldo.setter
    def saldo(self, nuevo_saldo):
        """
        Setter para la propiedad saldo con validación
        
        Args:
            nuevo_saldo (float): Nuevo saldo a establecer
        
        Raises:
            ValueError: Si el nuevo saldo es negativo
        """
        if nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = float(nuevo_saldo)
    
    def depositar(self, cantidad):
        """
        Deposita una cantidad en la cuenta
        
        Args:
            cantidad (float): Cantidad a depositar
        
        Returns:
            bool: True si la operación fue exitosa, False en caso contrario
        """
        if cantidad <= 0:
            return False
        self._saldo += cantidad
        return True
    
    def retirar(self, cantidad):
        """
        Retira una cantidad de la cuenta
        
        Args:
            cantidad (float): Cantidad a retirar
        
        Returns:
            bool: True si la operación fue exitosa, False en caso contrario
        """
        if cantidad <= 0 or cantidad > self._saldo:
            return False
        self._saldo -= cantidad
        return True
    
    def __str__(self):
        """
        Representación en cadena de la cuenta bancaria
        
        Returns:
            str: Información de la cuenta
        """
        return f"Cuenta de {self._titular}: ${self._saldo:.2f}"


# Programa de prueba para demostrar el funcionamiento
def main():
    print("=== TALLER DE ENCAPSULACIÓN - CUENTA BANCARIA ===\n")
    
    try:
        # Crear una cuenta bancaria
        print("1. Creando cuenta bancaria:")
        cuenta = CuentaBancaria("Juan Pérez", 1000)
        print(f"   {cuenta}")
        print()
        
        # Probar propiedad titular (solo lectura)
        print("2. Probando propiedad 'titular' (solo lectura):")
        print(f"   Titular: {cuenta.titular}")
        try:
            # Esto debería generar un error porque titular es de solo lectura
            # cuenta.titular = "Otro nombre"  # Descomenta para ver el error
            print("   ✓ La propiedad titular es de solo lectura")
        except AttributeError as e:
            print(f"   ✓ Error esperado: {e}")
        print()
        
        # Probar propiedad saldo (lectura y escritura con validación)
        print("3. Probando propiedad 'saldo':")
        print(f"   Saldo actual: ${cuenta.saldo:.2f}")
        
        # Intentar establecer saldo válido
        cuenta.saldo = 1500
        print(f"   Saldo después de establecer $1500: ${cuenta.saldo:.2f}")
        
        # Intentar establecer saldo negativo
        try:
            cuenta.saldo = -100
        except ValueError as e:
            print(f"   ✓ Error esperado al intentar saldo negativo: {e}")
        print()
        
        # Probar método depositar
        print("4. Probando método depositar:")
        resultado = cuenta.depositar(500)
        print(f"   Depósito de $500: {'Exitoso' if resultado else 'Fallido'}")
        print(f"   Saldo actual: ${cuenta.saldo:.2f}")
        
        resultado = cuenta.depositar(-100)
        print(f"   Intento de depósito negativo (-$100): {'Exitoso' if resultado else 'Fallido'}")
        print(f"   Saldo actual: ${cuenta.saldo:.2f}")
        
        resultado = cuenta.depositar(0)
        print(f"   Intento de depósito cero ($0): {'Exitoso' if resultado else 'Fallido'}")
        print(f"   Saldo actual: ${cuenta.saldo:.2f}")
        print()
        
        # Probar método retirar
        print("5. Probando método retirar:")
        resultado = cuenta.retirar(300)
        print(f"   Retiro de $300: {'Exitoso' if resultado else 'Fallido'}")
        print(f"   Saldo actual: ${cuenta.saldo:.2f}")
        
        resultado = cuenta.retirar(3000)  # Más dinero del disponible
        print(f"   Intento de retiro de $3000: {'Exitoso' if resultado else 'Fallido'}")
        print(f"   Saldo actual: ${cuenta.saldo:.2f}")
        
        resultado = cuenta.retirar(-50)  # Cantidad negativa
        print(f"   Intento de retiro negativo (-$50): {'Exitoso' if resultado else 'Fallido'}")
        print(f"   Saldo actual: ${cuenta.saldo:.2f}")
        print()
        
        # Crear otra cuenta con diferentes parámetros
        print("6. Creando segunda cuenta:")
        cuenta2 = CuentaBancaria("María González", 500)
        print(f"   {cuenta2}")
        
        # Realizar algunas operaciones
        cuenta2.depositar(200)
        cuenta2.retirar(150)
        print(f"   Después de depósito y retiro: {cuenta2}")
        print()
        
        # Intentar crear cuenta con saldo inicial negativo
        print("7. Intentando crear cuenta con saldo inicial negativo:")
        try:
            cuenta_invalida = CuentaBancaria("Pedro López", -100)
        except ValueError as e:
            print(f"   ✓ Error esperado: {e}")
        
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()