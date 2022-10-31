from json.tool import main
from peewee import *

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
          opcion = input('ingrese el numero:')


def dar_de_alta():
     return null

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

if __name__ =="__main__":
     pg_db = PostgresqlDatabase('dbd2', user='dbd2g1', password='dbd2#G1',
                           host='127.0.0.1', port=8888)

     

     