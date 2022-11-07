import Cuenta
from database import *
from peewee import *
 
class Tarjeta(BaseModel):
    nro_cuenta = IntegerField()
    tipo = CharField() 
    emisor = CharField()
    numero = IntegerField() 
    vencimiento = DateField()
        
    class Meta: 
        database= db_pg

