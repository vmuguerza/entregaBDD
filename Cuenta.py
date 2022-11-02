
from tempfile import gettempprefix
import Cliente
from datetime import date
from database import BaseModel
from peewee import *

 
class Cuenta(BaseModel):
    dni = IntegerField()
    usuario = CharField() 
    nro_cuenta = IntegerField()
    fecha_creacion = DateField()

    

