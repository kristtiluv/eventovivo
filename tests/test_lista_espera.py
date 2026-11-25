from datetime import datetime

import pytest

from eventovivo.lista_espera import posicion_en_espera, unirse_lista_espera
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


def test_queda_registrado_con_su_orden():
    sesiones = [crear_sesion(cupo=0)]
    inscritos: dict[int, set[str]] = {}
    espera: dict[int, list[str]] = {}

    unirse_lista_espera(sesiones, inscritos, espera, "ana@uleam.edu.ec", 1)
    unirse_lista_espera(sesiones, inscritos, espera, "luis@uleam.edu.ec", 1)

    assert espera[1] == ["ana@uleam.edu.ec", "luis@uleam.edu.ec"]


def test_puede_ver_su_posicion():
    sesiones = [crear_sesion(cupo=0)]
    inscritos: dict[int, set[str]] = {}
    espera: dict[int, list[str]] = {}

    unirse_lista_espera(sesiones, inscritos, espera, "ana@uleam.edu.ec", 1)
    mensaje = unirse_lista_espera(sesiones, inscritos, espera, "luis@uleam.edu.ec", 1)

    assert posicion_en_espera(espera, "ana@uleam.edu.ec", 1) == 1
    assert posicion_en_espera(espera, "luis@uleam.edu.ec", 1) == 2
    assert "posición: 2" in mensaje.lower()


def test_no_entra_a_la_lista_si_todavia_hay_cupo():
    sesiones = [crear_sesion(cupo=2)]
    inscritos: dict[int, set[str]] = {}
    espera: dict[int, list[str]] = {}

    mensaje = unirse_lista_espera(sesiones, inscritos, espera, "ana@uleam.edu.ec", 1)

    assert "cupo" in mensaje.lower()
    assert espera.get(1, []) == []


def test_no_se_duplica_en_la_lista():
    sesiones = [crear_sesion(cupo=0)]
    inscritos: dict[int, set[str]] = {}
    espera: dict[int, list[str]] = {}

    unirse_lista_espera(sesiones, inscritos, espera, "ana@uleam.edu.ec", 1)
    mensaje = unirse_lista_espera(sesiones, inscritos, espera, "ana@uleam.edu.ec", 1)

    assert espera[1] == ["ana@uleam.edu.ec"]
    assert "ya estás en la lista" in mensaje.lower()


def test_posicion_es_none_si_no_esta_en_la_lista():
    assert posicion_en_espera({}, "ana@uleam.edu.ec", 1) is None


def test_lista_de_espera_en_sesion_inexistente():
    sesiones = [crear_sesion(cupo=0)]

    with pytest.raises(ValueError):
        unirse_lista_espera(sesiones, {}, {}, "ana@uleam.edu.ec", 999)