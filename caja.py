import cuentaCliente
class Caja():
    escritorio=''
    cajaRegistrador=''
    idUbicacion=0
    saldoCuenta=0

    def __init__(self):
        self.idUbicacion=1111
        self.escritorio=True
        self.cajaRegistrador=True
        self.saldoCuenta=cuentaCliente.CuentaCliente()


        
laCaja=Caja()
#opcion indica que quiere hacer el cliente
opcion="comprarDoles"
#monto=8000
monto=100
if(opcion=="retiroPesos"):
    laCaja.saldoCuenta.sacoSaldoCuenta(monto)
if(opcion=="retiroDolares"):
    laCaja.saldoCuenta.sacoSaldoCuentaDolares(monto)
if(opcion=="comprarDoles"):
    laCaja.saldoCuenta.comproDoles(monto)
if(opcion=="vendoDolares"):
    laCaja.saldoCuenta.vendoDolares(monto)