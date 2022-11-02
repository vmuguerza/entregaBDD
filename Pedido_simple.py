from datetime import date
from database import BaseModel
from Producto import Producto
from peewee import *
 
class Pedido_simple (BaseModel):
    id = BigAutoField()
    #producto = codigo_producto         
    # #cantidad = cantidad 
    canal_de_compra = CharField() 
    nro_pedido_compuesto = IntegerField()   
    dni_cliente = IntegerField()
    precio_total = IntegerField()
    estado = CharField()
    fecha = DateField()

    def actualizar_stock(self):
        stock=(self._producto.get_stock()) - self._cantidad
        self._producto.set_stock(stock)

    def set_estado_rechazado(self):
        self._estado = 'rechazado'

    def set_estado_despachado(self):
        self._estado = 'despachado'
        self.actualizar_stock()

    def set_estado_entragado(self):
        self._estado = 'entregado'


        

        