from random import randint
class CuentaCliente():
    def __init__(self):
            self.saldoPesos=100000
            self.saldoDolaes=2000
            self.Nombre="Ricardo"
            self.idCliente=123456


    def muestroSaldoCuentaPesos(self):
        return print("Su saldo es: ",self.saldoPesos)
    def sacoSaldoCuenta(self,retiro):
        if(retiro<self.saldoPesos):
            self.saldoPesos=self.saldoPesos-retiro
            return print("Su saldo es: $",self.saldoPesos, " Usted retiro: $",retiro)
        else:
            return print("No tiene saldo suficiente")
    def pongoSaldoCuenta(self,deposito):
       self.saldoPesos=self.saldoPesos+deposito
       return print("Su saldo es: $",self.saldoPesos)
    def sacoSaldoCuentaDolares(self,retiro):
        if(retiro>self.saldoDolaes):
            return print("No tiene saldo suficiente")
        else:    
            self.saldoDolaes=self.saldoDolaes-retiro
            return print("Usted retiro: $",retiro," Su saldo de dolares es: ",self.saldoDolaes) 
    def comproDoles(self,cantidadDolares):
        montoConTC=cantidadDolares*185
        self.saldoDolaes=self.saldoDolaes+cantidadDolares
        self.saldoPesos=self.saldoPesos-montoConTC
        if(montoConTC<self.saldoPesos):
            return print("Su saldo en dolares ahora es: $",self.saldoDolaes)
        else:
            return print("No tiene los fondos suficientes")
    def vendoDolares(self,cantidadDolares):
        montoConTC=cantidadDolares*150
        self.saldoPesos=self.saldoPesos+montoConTC
        self.saldoDolaes=self.saldoDolaes-cantidadDolares
        if(cantidadDolares<self.saldoDolaes):
            return print("Su saldo en pesos es: $",self.saldoPesos)
        else:
            return print("No tiene saldo suficiente para vender dolares")
    #Genero clave Homebanking        
    def generoNuevaClaveHomeBanking(self):
        numeros_aleatorios = [randint(1,9) for i in range(20)]
        return numeros_aleatorios              