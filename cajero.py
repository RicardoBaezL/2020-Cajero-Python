from random import randint
import cuentaCliente
class Cajero():
    stado=False
    saldoPesos=cuentaCliente.cuentaCliente.saldoPesos
    
    def setEstado(self):
        self.stado=True    
    def getEstado(self):
        if(self.stado):
            return "El cajero esta activo"
        else:
            return "El cajero no esta activo"         
    def generoNuevaClaveHomeBanking(self):
        numeros_aleatorios = [randint(1,20) for i in range(20)]
        return numeros_aleatorios


elCajero=Cajero()
elCajero.setEstado()
saldoCuenta=cuentaCliente.cuentaCliente()
print(elCajero.getEstado())


opcion=3
if(opcion==1):
    print("Su saldo es: ",elCajero.saldoPesos)
if(opcion==2):
    retiro=100
    #retiro=10000000
    saldoCuenta.sacoSaldoCuenta(retiro)
if(opcion==3):
    depositoPlata=1000
    saldoCuenta.pongoSaldoCuenta(depositoPlata)
if(opcion==4):
    print("Su clave es: ",elCajero.generoNuevaClaveHomeBanking())