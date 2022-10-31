import Cuenta
from database import BaseModel
 
class Tarjeta(BaseModel):
    def __init__(self,nro_cuenta, tipo, emisor, numero):
        self._Cuenta = nro_cuenta 
        self._tipo = tipo 
        self._emisor = emisor
        self._numero = numero 
        
        
