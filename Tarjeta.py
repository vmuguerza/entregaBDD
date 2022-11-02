from Config import Config
import Cuenta
from database import BaseModel
from peewee import *
 
class Tarjeta(BaseModel):
    nro_cuenta = IntegerField()
    tipo = CharField() 
    emisor = CharField()
    numero = IntegerField() 
    vencimiento = DateField()
        
    class Meta: 
        database= Config.db_pg

