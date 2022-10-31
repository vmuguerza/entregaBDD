
from tempfile import gettempprefix
import Cliente
from datetime import date
from database import BaseModel

 
class Cuenta(BaseModel):
    
    def __init__ (self, dni_cliente, usuario, nro_cuenta):
        self._dni_cliente = dni_cliente
        self._usuario = usuario 
        self._nro_cuenta = nro_cuenta
        self._fecha_creacion = date.today()

    

