from eventovivo.modelos import Sesion


def inscribir_sesion(
    sesiones: list[Sesion],
    inscritos_por_sesion: dict[int, set[str]],
    participante: str,
    sesion_id: int,
) -> str:
    """HU-02: inscribe a un participante en una sesión si hay cupo disponible."""
    sesion = next((s for s in sesiones if s.id == sesion_id), None)
    if sesion is None:
        raise ValueError(f"No existe una sesión con id {sesion_id}.")

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