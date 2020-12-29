class cuentaCliente():
    saldoPesos=100000
    saldoDolaes=2000
    Nombre="Ricardo"

    def sacoSaldoCuenta(self,retiro):
        if(retiro<cuentaCliente.saldoPesos):
            cuentaCliente.saldoPesos=cuentaCliente.saldoPesos-retiro
            return print("Su saldo es: $",cuentaCliente.saldoPesos, " Usted reitor: $",retiro)
        else:
            return print("No tiene saldo suficiente")
    def pongoSaldoCuenta(self,deposito):
       cuentaCliente.saldoPesos=cuentaCliente.saldoPesos+deposito
       return print("Su saldo es: $",cuentaCliente.saldoPesos)
