from eventovivo.inscripcion import inscribir_sesion
from eventovivo.modelos import Sesion


def _se_superponen(a: Sesion, b: Sesion) -> bool:
    """Dos sesiones chocan si una empieza antes de que termine la otra."""
    return a.inicio < b.fin and b.inicio < a.fin


def buscar_choque(
    sesiones: list[Sesion],
    inscritos_por_sesion: dict[int, set[str]],
    participante: str,
    sesion_id: int,
) -> Sesion | None:
    """HU-03: devuelve la sesión inscrita que choca con la nueva, o None."""
    nueva = next((s for s in sesiones if s.id == sesion_id), None)
    if nueva is None:
        raise ValueError(f"No existe una sesión con id {sesion_id}.")

    for otra in sesiones:
        if otra.id == sesion_id:
            continue
        if participante in inscritos_por_sesion.get(otra.id, set()):
            if _se_superponen(nueva, otra):
                return otra
    return None


def inscribir_sin_choque(
    sesiones: list[Sesion],
    inscritos_por_sesion: dict[int, set[str]],
    participante: str,
    sesion_id: int,
) -> str:
    """HU-03: bloquea la inscripción si el horario choca con otra sesión."""
    choque = buscar_choque(sesiones, inscritos_por_sesion, participante, sesion_id)
    if choque is not None:
        return (
            f"No se puede inscribir: el horario choca con '{choque.titulo}' "
            f"({choque.inicio:%d/%m %H:%M} - {choque.fin:%H:%M})."
        )
    return inscribir_sesion(sesiones, inscritos_por_sesion, participante, sesion_id)