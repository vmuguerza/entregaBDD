from database import BaseModel
from peewee import *

class Pedido_compuesto(BaseModel):
    dni_cliente = IntegerField()
    id = BigAutoField() 
    fecha = DateField() 
    canal_de_compra = CharField()
        
    