from datetime import datetime
import pytest

from eventovivo.datos import SESIONES
from eventovivo.inscripcion import inscribir_sesion
from eventovivo.modelos import Sesion


def test_inscripcion_exitosa_reduce_cupo():
    sesiones = [
        Sesion(
            1,
            "Taller de Python",
            2,
            datetime(2026, 12, 1, 9, 0),
            datetime(2026, 12, 1, 11, 0),
            "Aula 101",
        )
    ]
    inscritos_por_sesion: dict[int, set[str]] = {}

    mensaje = inscribir_sesion(sesiones, inscritos_por_sesion, "ana@uleam.edu.ec", 1)

    assert "Inscripción confirmada" in mensaje
    assert sesiones[0].cupo == 1
    assert "ana@uleam.edu.ec" in inscritos_por_sesion[1]


def test_inscripcion_rechazada_sin_cupo():
    sesion_llena = Sesion(
        5,
        "Taller Lleno",
        0,
        datetime(2026, 12, 3, 9, 0),
        datetime(2026, 12, 3, 11, 0),
        "Aula 103",
    )
    sesiones = [sesion_llena]
    inscritos_por_sesion: dict[int, set[str]] = {}

    mensaje = inscribir_sesion(sesiones, inscritos_por_sesion, "luis@uleam.edu.ec", 5)

    assert "cupo" in mensaje.lower() or "lleno" in mensaje.lower() or "no disponible" in mensaje.lower()
    assert sesion_llena.cupo == 0


def test_inscripcion_duplicada_misma_sesion():
    sesiones = [SESIONES[0]]
    inscritos_por_sesion: dict[int, set[str]] = {1: {"ana@uleam.edu.ec"}}
    cupo_inicial = sesiones[0].cupo

    mensaje = inscribir_sesion(sesiones, inscritos_por_sesion, "ana@uleam.edu.ec", 1)

    assert "ya estás inscrito" in mensaje.lower() or "ya inscrito" in mensaje.lower()
    assert sesiones[0].cupo == cupo_inicial


def test_inscripcion_sesion_inexistente():
    sesiones = [SESIONES[0]]
    inscritos_por_sesion: dict[int, set[str]] = {}

    with pytest.raises(ValueError):
        inscribir_sesion(sesiones, inscritos_por_sesion, "ana@uleam.edu.ec", 999)