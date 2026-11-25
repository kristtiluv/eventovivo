from datetime import datetime

from eventovivo.choques import buscar_choque, inscribir_sin_choque
from eventovivo.inscripcion import inscribir_sesion
from eventovivo.modelos import Sesion


def crear_sesiones() -> list[Sesion]:
    return [
        Sesion(1, "Taller de Python", 5,
               datetime(2026, 12, 1, 9, 0), datetime(2026, 12, 1, 11, 0), "Aula 101"),
        Sesion(2, "Taller de Git", 5,
               datetime(2026, 12, 1, 10, 0), datetime(2026, 12, 1, 12, 0), "Aula 102"),
        Sesion(3, "Charla de Kanban", 5,
               datetime(2026, 12, 2, 10, 0), datetime(2026, 12, 2, 11, 0), "Auditorio"),
    ]


def test_bloquea_inscripcion_con_horario_superpuesto():
    sesiones = crear_sesiones()
    inscritos: dict[int, set[str]] = {}
    inscribir_sesion(sesiones, inscritos, "ana@uleam.edu.ec", 1)

    mensaje = inscribir_sin_choque(sesiones, inscritos, "ana@uleam.edu.ec", 2)

    assert "choca" in mensaje.lower()
    assert "ana@uleam.edu.ec" not in inscritos.get(2, set())
    assert sesiones[1].cupo == 5


def test_indica_con_que_sesion_choca():
    sesiones = crear_sesiones()
    inscritos: dict[int, set[str]] = {}
    inscribir_sesion(sesiones, inscritos, "ana@uleam.edu.ec", 1)

    mensaje = inscribir_sin_choque(sesiones, inscritos, "ana@uleam.edu.ec", 2)

    assert "Taller de Python" in mensaje


def test_permite_inscripcion_sin_choque():
    sesiones = crear_sesiones()
    inscritos: dict[int, set[str]] = {}
    inscribir_sesion(sesiones, inscritos, "ana@uleam.edu.ec", 1)

    mensaje = inscribir_sin_choque(sesiones, inscritos, "ana@uleam.edu.ec", 3)

    assert "confirmada" in mensaje.lower()
    assert "ana@uleam.edu.ec" in inscritos[3]
    assert sesiones[2].cupo == 4


def test_sesiones_consecutivas_no_chocan():
    sesiones = [
        Sesion(1, "Taller A", 5,
               datetime(2026, 12, 1, 9, 0), datetime(2026, 12, 1, 11, 0), "Aula 1"),
        Sesion(2, "Taller B", 5,
               datetime(2026, 12, 1, 11, 0), datetime(2026, 12, 1, 13, 0), "Aula 2"),
    ]
    inscritos: dict[int, set[str]] = {}
    inscribir_sesion(sesiones, inscritos, "ana@uleam.edu.ec", 1)

    assert buscar_choque(sesiones, inscritos, "ana@uleam.edu.ec", 2) is None


def test_sin_inscripciones_no_hay_choque():
    sesiones = crear_sesiones()
    inscritos: dict[int, set[str]] = {}

    assert buscar_choque(sesiones, inscritos, "ana@uleam.edu.ec", 2) is None