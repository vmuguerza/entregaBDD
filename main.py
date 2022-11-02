from json.tool import main
from peewee import *
from Cobro import Cobro
from Cuenta import Cuenta
from Funciones import *
from Pedido_compuesto import *
from Pedido_simple import Pedido_simple
from Producto import Producto
from Tarjeta import Tarjeta


pg_db = PostgresqlDatabase('dbd2', user='dbd2g1', password='dbd2#G1', host='localhost', port=8888)


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
     pg_db.connect()
     #pg_db.create_tables([Cliente, Cuenta, Cobro, Pedido_compuesto, Pedido_simple, Producto, Tarjeta])

     pg_db.create_tables([Cliente])
     pg_db.create_tables([Cuenta])
     pg_db.create_tables([Cobro])
     pg_db.create_tables([Pedido_compuesto])
     pg_db.create_tables([Pedido_simple])
     pg_db.create_tables([Producto])
     pg_db.create_tables([Tarjeta])


     while True:
          menu()

     