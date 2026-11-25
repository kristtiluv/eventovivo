from eventovivo.modelos import Sesion


def unirse_lista_espera(
    sesiones: list[Sesion],
    inscritos_por_sesion: dict[int, set[str]],
    lista_espera: dict[int, list[str]],
    participante: str,
    sesion_id: int,
) -> str:
    """HU-04: registra al participante en la lista de espera si la sesión está llena."""
    sesion = next((s for s in sesiones if s.id == sesion_id), None)
    if sesion is None:
        raise ValueError(f"No existe una sesión con id {sesion_id}.")

    if participante in inscritos_por_sesion.get(sesion_id, set()):
        return f"Ya estás inscrito en '{sesion.titulo}'."

    if sesion.cupo > 0:
        return f"Todavía hay cupo en '{sesion.titulo}': inscríbete directamente."

    fila = lista_espera.setdefault(sesion_id, [])
    if participante in fila:
        return f"Ya estás en la lista de espera de '{sesion.titulo}'."

    fila.append(participante)
    return (
        f"Quedaste en la lista de espera de '{sesion.titulo}'. "
        f"Tu posición: {len(fila)}."
    )


def posicion_en_espera(
    lista_espera: dict[int, list[str]],
    participante: str,
    sesion_id: int,
) -> int | None:
    """HU-04: devuelve la posición (desde 1) del participante, o None si no está."""
    fila = lista_espera.get(sesion_id, [])
    if participante in fila:
        return fila.index(participante) + 1
    return None