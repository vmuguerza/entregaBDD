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
     if opcion == 3:
     if opcion == 4:
     if opcion == 5:
     if opcion == 6:  

def dar_de_alta():
     

if __name__ =="__main__":
     pg_db = PostgresqlDatabase('dbd2', user='dbd2g1', password='dbd2#G1',
                           host='127.0.0.1', port=8888)

     

     