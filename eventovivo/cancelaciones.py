from eventovivo.modelos import Sesion, buscar_sesion


def cancelar_inscripcion(
    sesiones: list[Sesion],
    inscritos_por_sesion: dict[int, set[str]],
    participante: str,
    sesion_id: int,
) -> str:
    """HU-09: cancela la inscripción de un participante y libera su cupo."""
    sesion = buscar_sesion(sesiones, sesion_id)
    
    inscritos = inscritos_por_sesion.setdefault(sesion_id, set())
    if participante not in inscritos:
        return f"No estás inscrito en '{sesion.titulo}'."

    inscritos.remove(participante)
    sesion.cupo += 1
    return (
        f"Inscripción cancelada en '{sesion.titulo}'. "
        f"Cupo disponible: {sesion.cupo}."
    )