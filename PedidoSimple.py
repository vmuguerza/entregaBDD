from datetime import date
from Producto import Producto

class PedidoSimple:
    def __init__(self,(Producto) producto, cantidad, canalDeCompra, (PedidoCompuesto) PedidoCompuesto, (Cliente) Cliente):
        self._id = id
        self._producto = producto 
        self._cantidad = cantidad 
        self._canal_de_compra = canalDeCompra 
        self._pedido_compuesto = PedidoCompuesto
        self._cliente = Cliente 
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


        

        