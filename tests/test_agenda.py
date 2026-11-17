from eventovivo.agenda import listar_sesiones, mensaje_agenda
from eventovivo.datos import SESIONES


def test_muestra_cupo_horario_y_ubicacion():
    texto = mensaje_agenda(SESIONES)
    assert "Cupo: 20" in texto
    assert "09:00" in texto
    assert "Aula 101" in texto


def test_sesiones_ordenadas_por_inicio():
    inicios = [s.inicio for s in listar_sesiones(SESIONES)]
    assert inicios == sorted(inicios)


def test_sin_sesiones_muestra_mensaje_claro():
    assert mensaje_agenda([]) == "No hay sesiones disponibles por ahora."
