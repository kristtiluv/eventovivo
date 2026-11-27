from eventovivo.modelos import Sesion, buscar_sesion


def inscribir_sesion(
    sesiones: list[Sesion],
    inscritos_por_sesion: dict[int, set[str]],
    participante: str,
    sesion_id: int,
) -> str:
    """HU-02: inscribe a un participante en una sesión si hay cupo disponible."""
    sesion = buscar_sesion(sesiones, sesion_id)

    inscritos = inscritos_por_sesion.setdefault(sesion_id, set())
    if participante in inscritos:
        return f"Ya estás inscrito en '{sesion.titulo}'."

    if sesion.cupo <= 0:
        return f"No hay cupo disponible para '{sesion.titulo}'."

    inscritos.add(participante)
    sesion.cupo -= 1
    return (
        f"Inscripción confirmada en '{sesion.titulo}' "
        f"({sesion.inicio:%d/%m %H:%M} - {sesion.ubicacion}). "
        f"Cupo restante: {sesion.cupo}."
    )