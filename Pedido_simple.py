from datetime import date
from database import BaseModel
from Producto import Producto
 
class PedidoSimple (BaseModel):
    def __init__(self, codigo_producto, cantidad, canalDeCompra, id_pedido_compuesto, dni_cliente):
        self._id = id
        self._producto = codigo_producto 
        self._cantidad = cantidad 
        self._canal_de_compra = canalDeCompra 
        self._pedido_compuesto = id_pedido_compuesto
        self._cliente = dni_cliente 
        self._precio_total = (self._cantidad)*(self._producto.getprecio())
        self._estado = 'confirmado'
        self._date = date.today()

    def actualizar_stock(self):
        stock=(self._producto.get_stock()) - self._cantidad
        self._producto.set_stock(stock)

    def set_estado_rechazado(self):
        self._estado = 'rechazado'

    def set_estado_despachado(self):
        self._estado = 'despachado'
        self.actualizar_stock()

    def set_estado_entragado(self):
        self._estado = 'entregado'


        

        