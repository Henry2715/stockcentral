import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from producto import Producto, StockInsuficienteError
from venta import VentaService, DashboardService


def test_registrar_producto_valido():
    p = Producto(1, "Camiseta básica", 15.99, 40, "Ropa")
    assert p.nombre == "Camiseta básica"
    assert p.stock == 40


def test_registrar_producto_precio_invalido():
    with pytest.raises(ValueError):
        Producto(2, "Pantalón jean", -5, 10, "Ropa")


def test_registrar_producto_nombre_vacio():
    with pytest.raises(ValueError):
        Producto(3, "   ", 20, 10, "Ropa")


def test_venta_con_stock_suficiente_descuenta_stock():
    p = Producto(4, "Gorra", 9.99, 80, "Accesorios")
    service = VentaService()
    venta = service.registrar_venta(p, 5, usuario="empleado1")
    assert p.stock == 75
    assert venta.cantidad == 5
    assert venta.precio_al_momento == 9.99


def test_venta_con_stock_insuficiente_se_rechaza():
    p = Producto(5, "Zapatos deportivos", 59.99, 3, "Calzado")
    service = VentaService()
    with pytest.raises(StockInsuficienteError):
        service.registrar_venta(p, 10, usuario="empleado1")
    assert p.stock == 3  # el stock NO debe modificarse si la venta se rechaza


def test_venta_cantidad_cero_se_rechaza():
    p = Producto(6, "Bufanda", 12.50, 20, "Accesorios")
    service = VentaService()
    with pytest.raises(ValueError):
        service.registrar_venta(p, 0, usuario="empleado1")


def test_precio_historico_no_cambia_si_producto_se_reprecia():
    p = Producto(7, "Chaqueta", 80.0, 10, "Ropa")
    service = VentaService()
    venta = service.registrar_venta(p, 1, usuario="empleado1")
    p.precio = 95.0  # la dueña sube el precio después
    assert venta.precio_al_momento == 80.0  # la venta histórica no cambia


def test_dashboard_cuenta_productos_bajo_stock():
    productos = [
        Producto(8, "Medias", 3.0, 5, "Accesorios"),   # bajo stock
        Producto(9, "Correa", 25.0, 50, "Accesorios"), # normal
        Producto(10, "Gorro", 7.0, 9, "Accesorios"),   # bajo stock
    ]
    dash = DashboardService(productos)
    bajos = dash.productos_bajo_stock(umbral=10)
    assert dash.total_productos() == 3
    assert len(bajos) == 2
    assert {p.nombre for p in bajos} == {"Medias", "Gorro"}
