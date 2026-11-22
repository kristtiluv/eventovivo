from datetime import datetime

import pytest

from eventovivo.cancelaciones import cancelar_inscripcion
from eventovivo.inscripcion import inscribir_sesion
from eventovivo.modelos import Sesion


def crear_sesion(cupo: int) -> Sesion:
    return Sesion(
        1,
        "Taller de Python",
        cupo,
        datetime(2026, 12, 1, 9, 0),
        datetime(2026, 12, 1, 11, 0),
        "Aula 101",
    )


def test_cancelar_libera_el_cupo_al_instante():
    sesion = crear_sesion(cupo=1)
    sesiones = [sesion]
    inscritos: dict[int, set[str]] = {}
    inscribir_sesion(sesiones, inscritos, "ana@uleam.edu.ec", 1)
    assert sesion.cupo == 0

    mensaje = cancelar_inscripcion(sesiones, inscritos, "ana@uleam.edu.ec", 1)

    assert sesion.cupo == 1
    assert "ana@uleam.edu.ec" not in inscritos[1]
    assert "cancelada" in mensaje.lower()


def test_no_permite_cancelar_dos_veces():
    sesion = crear_sesion(cupo=1)
    sesiones = [sesion]
    inscritos: dict[int, set[str]] = {}
    inscribir_sesion(sesiones, inscritos, "ana@uleam.edu.ec", 1)
    cancelar_inscripcion(sesiones, inscritos, "ana@uleam.edu.ec", 1)
    cupo_tras_primera = sesion.cupo

    mensaje = cancelar_inscripcion(sesiones, inscritos, "ana@uleam.edu.ec", 1)

    assert sesion.cupo == cupo_tras_primera
    assert "no estás inscrito" in mensaje.lower()


def test_cancelar_sin_haberse_inscrito_no_cambia_el_cupo():
    sesion = crear_sesion(cupo=2)
    sesiones = [sesion]
    inscritos: dict[int, set[str]] = {}

    mensaje = cancelar_inscripcion(sesiones, inscritos, "luis@uleam.edu.ec", 1)

    assert sesion.cupo == 2
    assert "no estás inscrito" in mensaje.lower()


def test_cancelar_en_sesion_inexistente():
    sesiones = [crear_sesion(cupo=1)]
    inscritos: dict[int, set[str]] = {}

    with pytest.raises(ValueError):
        cancelar_inscripcion(sesiones, inscritos, "ana@uleam.edu.ec", 999)