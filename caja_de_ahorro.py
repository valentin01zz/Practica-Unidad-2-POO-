class CajadeAhorro:
    nroCuenta: str
    cuil: str
    apellido: str
    nombre: str
    saldo: float

    def __init__(self, nroCuenta, cuil, apellido, nombre, saldo):
        self.nroCuenta = nroCuenta
        self.cuil = cuil
        self.apellido = apellido
        self.nombre = nombre
        self.saldo = saldo
    
    def mostrarDatos(self):
        print(self.nroCuenta, self.cuil, self.apellido, self.nombre, self.saldo)

    def extraer(self, importe):
        resultado = -1
        if importe <= self.saldo:
            self.saldo -= importe
            resultado = self.saldo
        return resultado

    def depositar(self, importe):
        if importe > 0:
            self.saldo += importe
        else:
            print('Ingrese un monto valido')

    def obtenerSaldo(self):
        return self.saldo

    def obtenerNombre(self):
        return self.nombre

    def obtenerApellido(self):
        return self.apellido

    def obtenercuil(self):
        return self.cuil

    def validarCuil(self, cuil):
        if len(cuil) != 11:  
            return False
        
        c1 = int(cuil[0]) * 5
        c2 = int(cuil[1]) * 4
        c3 = int(cuil[2]) * 3
        c4 = int(cuil[3]) * 2
        c5 = int(cuil[4]) * 7
        c6 = int(cuil[5]) * 6
        c7 = int(cuil[6]) * 5
        c8 = int(cuil[7]) * 4
        c9 = int(cuil[8]) * 3
        c10 = int(cuil[9]) * 2
        
        resultado = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10

        resto = resultado % 11

        if resto == 0:
            digito_verificador = 0
        else:
            digito_verificador = 11 - resto
        
        return digito_verificador == int(cuil[10])

def test():
    cuentas = []
    for i in range(3):
        nombre = input('\nIngrese su nombre: ')
        apellido = input('\nIngrese su apellido: ')
        cuil = input('\nIngrese su cuil: ')
        saldo = float(input('\nIngrese su saldo: '))
        cuenta = CajadeAhorro(str(i+1), cuil, apellido, nombre, saldo)
        cuentas.append(cuenta)

    for cuenta in cuentas:
        print("\nDatos de la cuenta:")
        cuenta.mostrarDatos()
        print("CUIL valido:", cuenta.validarCuil(cuenta.cuil))
        print("Saldo actual:", cuenta.obtenerSaldo())
        importe = float(input("\nIngrese el monto a depositar: "))
        cuenta.depositar(importe)
        print("Nuevo saldo despues del deposito:", cuenta.obtenerSaldo())
        importe = float(input("\nIngrese el monto a extraer: "))
        saldo_restante = cuenta.extraer(importe)
        if saldo_restante == -1:
            print("El monto a extraer es mayor que el saldo disponible.")
        else:
            print("Nuevo saldo despues de la extraccion:", saldo_restante)


if __name__ == "__main__":
    test()
