import cuentaCliente
class Caja():
    escritorio=True
    cajaRegistrador=True
    idUbicacion=1111
saldoCuenta=cuentaCliente.CuentaCliente()
#Indica cliente si quiere reirar pesos o dolares
opcion="vendoDolares"
#monto=8000
monto=100
if(opcion=="pesos"):
    saldoCuenta.sacoSaldoCuenta(monto)
if(opcion=="dolares"):
    saldoCuenta.sacoSaldoCuentaDolares(monto)
if(opcion=="comprarDoles"):
    saldoCuenta.comproDoles(monto)
if(opcion=="vendoDolares"):
    saldoCuenta.vendoDolares(monto)