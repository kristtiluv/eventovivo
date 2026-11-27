from datetime import datetime

from eventovivo.datos import SESIONES
from eventovivo.modelos import Sesion, buscar_sesion, tiene_cupo


def test_las_sesiones_ficticias_tienen_cupo_positivo():
    assert all(s.cupo > 0 for s in SESIONES)


def _sesion(cupo):
    return Sesion(1, "Taller", cupo, datetime(2026, 12, 1, 9, 0),
                  datetime(2026, 12, 1, 11, 0), "Aula 1")


def test_tiene_cupo_con_cupo_disponible():
    assert tiene_cupo(_sesion(2)) is True


def test_tiene_cupo_sin_cupo():
    assert tiene_cupo(_sesion(0)) is False


def test_buscar_sesion_devuelve_la_sesion():
    s = _sesion(3)
    assert buscar_sesion([s], 1) is s