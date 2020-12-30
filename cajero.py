import cuentaCliente
class Cajero():
    stado=False
    idCajero=1234567
    
    def setEstado(self):
        self.stado=True    
    def getEstado(self):
        if(self.stado):
            return "El cajero esta activo"
        else:
            return "El cajero no esta activo"         
       
elCajero=Cajero()
elCajero.setEstado()
Cuenta=cuentaCliente.CuentaCliente()
#indico el estado del cajero
#print(elCajero.getEstado())
opcion=1
if(opcion==1):
    print("Su saldo es: ",cuentaCliente.CuentaCliente.saldoPesos)
if(opcion==2):
    retiro=100
    #retiro=10000000
    Cuenta.sacoSaldoCuenta(retiro)
if(opcion==3):
    depositoPlata=1000
    Cuenta.pongoSaldoCuenta(depositoPlata)
if(opcion==4):
    print("Su clave es: ",Cuenta.generoNuevaClaveHomeBanking())