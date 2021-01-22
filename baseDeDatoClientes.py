import sqlite3

baseClientes=sqlite3.connect("datosClientes")
puntero=baseClientes.cursor()
#puntero.execute('''CREATE TABLE BDCLIENTES (
    #idCliente INTEGER PRIMARY KEY AUTOINCREMENT,
    #nombreCliente VARCHAR(80),
    #saldoCuentaPesos INTEGER,
    #saldoCuentaDolares INTEGER)
#''')
listadoClientes=[
    ("Ricardo Baez",100000,2000,),
    ("Gustavo Lopez",2000,100,),
    ("Monica Gutierrez",5000,80000,),
    ("Javier Ortega",3000,8000,),
    ("Luis Sanchez",40000,500,)
]
#puntero.executemany("INSERT INTO BDCLIENTES VALUES (NULL,?,?,?)",listadoClientes)
puntero.execute("SELECT * FROM BDCLIENTES")
verListaCliente=puntero.fetchall()
for cliente in verListaCliente:
    print("numero de id: ",cliente[0]," nombre cliente: ",cliente[1]," saldo en pesos es: ",cliente[2]," Saldo en dolares es: ",cliente[3],)
baseClientes.commit()
baseClientes.close()