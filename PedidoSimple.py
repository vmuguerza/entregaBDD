from datetime import date

class PedidoSimple:
    def __init__(self,(Producto)producto, cantidad, canalDeCompra, (PedidoCompuesto) PedidoCompuesto, (Cliente) Cliente):
        self._id = id
        self._producto = producto 
        self._cantidad = cantidad 
        self._canal_de_compra = canalDeCompra 
        self._pedido_compuesto = PedidoCompuesto
        self._cliente = Cliente 
        self._precio_total = (self._cantidad)*(self._producto.getprecio())
        self._estado = 'confirmado'
        self._date = date.today()

        