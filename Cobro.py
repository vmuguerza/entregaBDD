import Pedido_simple
import Cuenta
from database import BaseModel
from peewee import *

class Cobro (BaseModel): 
    id_pedido= BigAutoField()
    nro_cuenta = IntegerField()
    aprobado = BooleanField()
    nro_apruebacion = IntegerField() 
