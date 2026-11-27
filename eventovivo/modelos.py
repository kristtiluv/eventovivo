from dataclasses import dataclass
from datetime import datetime


@dataclass
class Sesion:
    """Una sesión de EventoVivo (taller, hackatón o encuentro)."""
    id: int
    titulo: str
    cupo: int
    inicio: datetime
    fin: datetime
    ubicacion: str

def buscar_sesion(sesiones: list[Sesion], sesion_id: int) -> Sesion:
    sesion = next((s for s in sesiones if s.id == sesion_id), None)
    if sesion is None:
        raise ValueError(f"No existe una sesión con id {sesion_id}.")
    return sesion

def tiene_cupo(sesion: Sesion) -> bool:
    return sesion.cupo > 0