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
