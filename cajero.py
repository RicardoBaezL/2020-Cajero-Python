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
    def sacoSaldoCuenta(self,retiro):
        if(retiro<elCajero.saldoPesos):
            elCajero.saldoPesos=elCajero.saldoPesos-retiro
            return print("Su saldo es: $",elCajero.saldoPesos, " Usted reitor: $",retiro)
        else:
            return print("No tiene saldo suficiente")      
    def pongoSaldoCuenta(self,deposito):
       elCajero.saldoPesos=elCajero.saldoPesos+deposito
    
    def generoNuevaClaveHomeBanking(self):
        numeros_aleatorios = [randint(1,20) for i in range(20)]
        return numeros_aleatorios


elCajero=Cajero()
elCajero.setEstado()
print(elCajero.getEstado())

opcion=2

if(opcion==1):
    print("Su saldo es: ",elCajero.saldoPesos)
if(opcion==2):
    retiro=100
    #retiro=10000000
    elCajero.sacoSaldoCuenta(retiro) 
if(opcion==3):
    depositoPlata=1000
    elCajero.pongoSaldoCuenta(depositoPlata)
    print(elCajero.saldoPesos)
if(opcion==4):
    print("Su clave es: ",elCajero.generoNuevaClaveHomeBanking())