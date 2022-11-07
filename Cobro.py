import Pedido_simple
import Cuenta
from database import *
from peewee import *

class Cobro (BaseModel): 
    id_pedido= BigAutoField()
    nro_cuenta = IntegerField()
    aprobado = BooleanField()
    nro_apruebacion = IntegerField() 

    class Meta: 
        database= db_pg

