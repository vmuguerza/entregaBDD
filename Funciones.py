from Cliente import Cliente


def dar_de_alta():
     print('Nuevo cliente:')
     nombre=input('ingrese el nombre:')
     apellido=input('ingrese el apellido:')
     dni=input('ingrese el DNI:')
     mail=input('ingrese el mail:')
     telefono=input('ingrese el telefono:')
     calle=input('ingrese la calle:')
     nro_puerta=input('ingrese el numero de puerta:')
     apto=input('ingrese el apartamento (si corresponde):')
     localidad = input('ingrese la localidad:')
     depto= input('ingrese el departamento:')
     cod_postal = input('ingrese el codigo postal:')
     nuevo=Cliente(nombre,apellido,dni,mail,depto,localidad,calle,nro_puerta,apto,cod_postal,telefono)



def dar_de_baja():
     return null   

def modificar():
     return null   

def ingresar_pedido():
     return null  

def ingresar_stock():
     return null  

def registrar_pago():
     return null  

def error(): 
    print("\nUno o más datos ingresados son inválidos, intente nuevamente\n")
    return
