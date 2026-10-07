# StockCentral

Sistema de gestion de inventario y dashboard administrativo para Boutique El Manantial (proyecto integrador de Ingenieria de Software I).

## Archivos
- `producto.py` — entidad Producto con validacion de precio/nombre y reglas de stock (RF-01).
- `venta.py` — VentaService (registro de venta con descuento de stock, RF-02) y DashboardService (conteo de bajo stock, RF-03).
- `tests/test_stockcentral.py` — suite de pruebas unitarias (pytest) de los dos modulos anteriores.
- `dashboard.html` — vista del dashboard administrativo (evidencia visual, FPI-16).
- `formulario.html` — vista de registrar producto / registrar venta (evidencia visual, FPI-06).

## Correr las pruebas
```
pip install pytest
pytest tests/ -v
```
