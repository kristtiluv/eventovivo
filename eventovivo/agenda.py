from eventovivo.modelos import Sesion


def listar_sesiones(sesiones: list[Sesion]) -> list[Sesion]:
    """HU-01: devuelve las sesiones ordenadas por fecha de inicio."""
    return sorted(sesiones, key=lambda s: s.inicio)


def mensaje_agenda(sesiones: list[Sesion]) -> str:
    """Texto que ve el participante. Si no hay sesiones, un mensaje claro."""
    if not sesiones:
        return "No hay sesiones disponibles por ahora."
    lineas = []
    for s in listar_sesiones(sesiones):
        lineas.append(
            f"{s.titulo} | {s.inicio:%d/%m %H:%M} | Cupo: {s.cupo} | {s.ubicacion}"
        )
    return "\n".join(lineas)
