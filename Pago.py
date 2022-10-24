import PedidoSimple
import Cuenta

class Pago:

    def __init__(self,(PedidoSimple)pedido, (Cuenta)cuenta):
        self._pedido = pedido 
        self._cuenta = cuenta 
        self._aprobado = False
        self._nro_operacion = nro 
