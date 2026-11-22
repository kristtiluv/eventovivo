from eventovivo.modelos import Sesion


def cancelar_inscripcion(
    sesiones: list[Sesion],
    inscritos_por_sesion: dict[int, set[str]],
    participante: str,
    sesion_id: int,
) -> str:
    """HU-09: cancela la inscripción de un participante y libera su cupo."""
    sesion = next((s for s in sesiones if s.id == sesion_id), None)
    if sesion is None:
        raise ValueError(f"No existe una sesión con id {sesion_id}.")

    inscritos = inscritos_por_sesion.setdefault(sesion_id, set())
    if participante not in inscritos:
        return f"No estás inscrito en '{sesion.titulo}'."

    inscritos.remove(participante)
    sesion.cupo += 1
    return (
        f"Inscripción cancelada en '{sesion.titulo}'. "
        f"Cupo disponible: {sesion.cupo}."
    )