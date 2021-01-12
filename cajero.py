import cuentaCliente
class Cajero():
    def __init__(self):
        self.stado=True
        self.idCajero=1234567
        self.Cuenta=cuentaCliente.CuentaCliente()
    
    def getEstado(self):
        if(self.stado):
            return "El cajero esta activo"
        else:
            return "El cajero no esta activo"         
       
elCajero=Cajero()


#indico el estado del cajero
#print(elCajero.getEstado())
opcion=4
if(opcion==1):
    elCajero.Cuenta.muestroSaldoCuentaPesos()
if(opcion==2):
    retiro=100
    #retiro=10000000
    elCajero.Cuenta.sacoSaldoCuenta(retiro)
if(opcion==3):
    depositoPlata=1000
    elCajero.Cuenta.pongoSaldoCuenta(depositoPlata)
if(opcion==4):
    print("Su clave es: ",elCajero.Cuenta.generoNuevaClaveHomeBanking())