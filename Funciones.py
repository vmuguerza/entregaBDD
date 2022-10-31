import Cliente


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
     return



def dar_de_baja():
     print('Dar de baja cliente:')
     din=input('ingrese el dni del cliente:')
     return None

def modificar():
     cliente=input('Ingrese el DNI del cliente que desea modificar')
     opcion=input('Ingrese que datos del cliente desea modificar')
     
     
     if opcion==1:
          mail=input('ingrese el mail:')
          cliente.set_mail(mail)
     if opcion==2:
          telefono=input('ingrese el telefono:')
          cliente.set_telefono(telefono)

     if opcion==3:
          calle=input('ingrese la calle:')
          nro_puerta=input('ingrese el numero de puerta:')
          apto=input('ingrese el apartamento (si corresponde):')
          localidad = input('ingrese la localidad:')
          depto= input('ingrese el departamento:')
          cod_postal = input('ingrese el codigo postal:')
          cliente.set_calle(calle)
          cliente.set_calle(nro_puerta)
          cliente.set_calle(apto)
          cliente.set_calle(localidad)
          cliente.set_calle(depto)
          cliente.set_calle(cod_postal)
          
     return

def ingresar_pedido():
     print('Ingresar pedido')
     producto=input('')
     cantidad=input('')
     nuevo_pedido=PedidoSimple(producto,cantidad,'aplicacion',None,cliente)
     print('pedido confirmado, el precio total es:',nuevo_pedido.get_precio_total)
     return None  

def ingresar_stock():
     producto=input('Ingrese el codigo del producto que deaea actualizar stock:')
     producto.set_stock(input('Ingrese el nuevo stock'))
     return None  

def registrar_pago():
     return None  

def error(): 
    print("\nUno o más datos ingresados son inválidos, intente nuevamente\n")
    return
