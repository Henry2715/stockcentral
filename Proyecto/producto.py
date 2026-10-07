class StockInsuficienteError(Exception):
    pass

class Producto:
    def __init__(self, id, nombre, precio, stock, categoria):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def tiene_stock_suficiente(self, cantidad):
        return self.stock >= cantidad

    def descontar_stock(self, cantidad):
        if not self.tiene_stock_suficiente(cantidad):
            raise StockInsuficienteError(
                f"Stock insuficiente para {self.nombre}: disponible {self.stock}, solicitado {cantidad}"
            )
        self.stock -= cantidad

    def esta_bajo_stock(self, umbral=10):
        return self.stock < umbral
