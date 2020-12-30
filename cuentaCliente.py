from random import randint
class CuentaCliente():
    saldoPesos=100000
    saldoDolaes=2000
    Nombre="Ricardo"
    idCliente=123456

    def sacoSaldoCuenta(self,retiro):
        if(retiro<CuentaCliente.saldoPesos):
            CuentaCliente.saldoPesos=CuentaCliente.saldoPesos-retiro
            return print("Su saldo es: $",CuentaCliente.saldoPesos, " Usted retiro: $",retiro)
        else:
            return print("No tiene saldo suficiente")
    def pongoSaldoCuenta(self,deposito):
       CuentaCliente.saldoPesos=CuentaCliente.saldoPesos+deposito
       return print("Su saldo es: $",CuentaCliente.saldoPesos)
    def sacoSaldoCuentaDolares(self,retiro):
        if(retiro>CuentaCliente.saldoDolaes):
            return print("No tiene saldo suficiente")
        else:    
            CuentaCliente.saldoDolaes=CuentaCliente.saldoDolaes-retiro
            return print("Usted retiro: $",retiro," Su saldo de dolares es: ",CuentaCliente.saldoDolaes) 
    def comproDoles(self,cantidadDolares):
        montoConTC=cantidadDolares*185
        CuentaCliente.saldoDolaes=CuentaCliente.saldoDolaes+cantidadDolares
        CuentaCliente.saldoPesos=CuentaCliente.saldoPesos-montoConTC
        if(montoConTC<CuentaCliente.saldoPesos):
            return print("Su saldo en dolares ahora es: $",CuentaCliente.saldoDolaes)
        else:
            return print("No tiene los fondos suficientes")
    def vendoDolares(self,cantidadDolares):
        montoConTC=cantidadDolares*150
        CuentaCliente.saldoPesos=CuentaCliente.saldoPesos+montoConTC
        CuentaCliente.saldoDolaes=CuentaCliente.saldoDolaes-cantidadDolares
        if(cantidadDolares<CuentaCliente.saldoDolaes):
            return print("Su saldo en pesos es: $",CuentaCliente.saldoPesos)
        else:
            return print("No tiene saldo suficiente para vender dolares")
    #Genero clave Homebanking        
    def generoNuevaClaveHomeBanking(self):
        numeros_aleatorios = [randint(1,9) for i in range(20)]
        return numeros_aleatorios
               