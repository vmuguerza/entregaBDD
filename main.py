from json.tool import main
from peewee import *
from database import *
from Cliente import *
from Cuenta import Cuenta
from Cobro import Cobro
from Pedido_compuesto import *
from Pedido_simple import Pedido_simple
from Producto import Producto
from Tarjeta import Tarjeta
from Funciones import *

def menu():
     print('Eliga una de las siguientes opciones:')
     print('1. Dar de alta')
     print('2. Dar de baja')
     print('3. Modificar')
     print('4. Ingresar pedido')
     print('5. Ingresar stock')
     print('6. Registrar pago')
     opcion = input('ingrese el numero:')

     if opcion == 1:
          dar_de_alta()
     if opcion == 2:
          dar_de_baja()
     if opcion == 3:
          modificar()
     if opcion == 4:
          ingresar_pedido()
     if opcion == 5:
          ingresar_stock()
     if opcion == 6:  
          registrar_pago()
     else:
          error()


if __name__ =="__main__":
     db_pg.connect()
     #pg_db.create_tables([Cliente, Cuenta, Cobro, Pedido_compuesto, Pedido_simple, Producto, Tarjeta])

     db_pg.create_tables([Cliente])
     db_pg.create_tables([Cuenta])
     db_pg.create_tables([Cobro])
     db_pg.create_tables([Pedido_compuesto])
     db_pg.create_tables([Pedido_simple])
     db_pg.create_tables([Producto])
     db_pg.create_tables([Tarjeta])
 
     while True:
          menu()
     