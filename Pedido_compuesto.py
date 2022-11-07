from database import *
from peewee import *

class Pedido_compuesto(BaseModel):
    dni_cliente = IntegerField()
    id = BigAutoField() 
    fecha = DateField() 
    canal_de_compra = CharField()

    class Meta: 
        database= db_pg

        
    