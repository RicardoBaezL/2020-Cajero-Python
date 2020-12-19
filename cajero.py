from random import randint

class Cajero():
    stado=False
    saldo=10000
    
    def setEstado(self):
        self.stado=True
    
    def getEstado(self):
        if(self.stado):
            return "El cajero esta activo"
        else:
            return "El cajero no esta activo"

    def sacoSaldoCuenta(self,retiro):
       self.saldo=self.saldo-retiro
       
    def pongoSaldoCuenta(self,deposito):
       self.saldo=self.saldo+deposito
    
    def generoNuevaClaveHomeBanking(self):
        numeros_aleatorios = [randint(1,20) for i in range(20)]
        return numeros_aleatorios


elCajero=Cajero()
elCajero.setEstado()
print(elCajero.getEstado())

opcion=4

if(opcion==1):
    print("Su saldo es: ",elCajero.saldo)
if(opcion==2):
    retiro=100
    #retiro=10000000
    elCajero.sacoSaldoCuenta(retiro)
    if(retiro<elCajero.saldo):
        print("Su saldo es: $",elCajero.saldo, " Usted reitor: $",retiro)
    else:
        print("No tiene saldo suficiente")  
if(opcion==3):
    depositoPlata=1000
    elCajero.pongoSaldoCuenta(depositoPlata)
    print(elCajero.saldo)
if(opcion==4):
    print("Su clave es: ",elCajero.generoNuevaClaveHomeBanking())