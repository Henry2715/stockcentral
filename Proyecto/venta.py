from datetime import date
from producto import StockInsuficienteError

class Venta:
    def __init__(self, id, producto, cantidad, usuario):
        self.id = id
        self.producto = producto
        self.cantidad = cantidad
        self.precio_al_momento = producto.precio
        self.fecha = date.today()
        self.usuario = usuario

class VentaService:
    def __init__(self):
        self.ventas = []
        self._contador = 1

    def registrar_venta(self, producto, cantidad, usuario):
        if cantidad <= 0:
            raise ValueError("La cantidad vendida debe ser mayor a 0")
        producto.descontar_stock(cantidad)  # lanza StockInsuficienteError si no alcanza
        venta = Venta(self._contador, producto, cantidad, usuario)
        self.ventas.append(venta)
        self._contador += 1
        return venta


class DashboardService:
    def __init__(self, productos):
        self.productos = productos

    def total_productos(self):
        return len(self.productos)

    def productos_bajo_stock(self, umbral=10):
        return [p for p in self.productos if p.esta_bajo_stock(umbral)]
