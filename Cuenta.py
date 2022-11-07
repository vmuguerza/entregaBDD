
from tempfile import gettempprefix
import Cliente
from datetime import date
from database import *
from peewee import *

 
class Cuenta(BaseModel):
    dni = IntegerField()
    usuario = CharField() 
    nro_cuenta = IntegerField()
    fecha_creacion = DateField()

    class Meta: 
        database= db_pg


