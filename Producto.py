
from database import BaseModel
from peewee import *

class Producto(BaseModel):
    cod_producto = BigAutoField() 
    nombre = CharField()
    stock = IntegerField() 
    precio = IntegerField() 
    qr = IntegerField() 

    def get_precio(self):
        return self._precio

    def set_precio(self,nuevo_precio):
        self._precio = nuevo_precio

    def get_stock(self):
        return self._stock
    
    def set_stock(self, nuevo_stock):
        self._stock = nuevo_stock
