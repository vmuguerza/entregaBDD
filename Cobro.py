import PedidoSimple
import Cuenta
from database import BaseModel

class Cobro (BaseModel):
 
    def __init__(self,id_pedido_simple, nro_cuenta,nro):
        self._pedido = id_pedido_simple 
        self._cuenta = nro_cuenta 
        self._aprobado = False
        self._nro_operacion = nro 
