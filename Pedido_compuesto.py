from database import BaseModel


class PedidoCompuesto(BaseModel):
    
    def __init__(self,dni_cliente, fecha, canalDeCompra):
        self._dni_cliente = dni_cliente 
        self._id = id #como se genera 
        self._fecha = fecha 
        self._canal_de_compra = canalDeCompra
        
    