from datetime import datetime

from eventovivo.modelos import Sesion

# Datos ficticios para probar. No son personas ni eventos reales.
SESIONES = [
    Sesion(1, "Taller de Python", 20,
           datetime(2026, 12, 1, 9, 0), datetime(2026, 12, 1, 11, 0), "Aula 101"),
    Sesion(2, "Hackatón de ideas", 15,
           datetime(2026, 12, 1, 14, 0), datetime(2026, 12, 1, 18, 0), "Laboratorio 2"),
    Sesion(3, "Charla de Kanban", 30,
           datetime(2026, 12, 2, 10, 0), datetime(2026, 12, 2, 11, 0), "Auditorio"),
    # Choca a propósito con el Taller de Python, para probar HU-03.
    Sesion(4, "Taller de Git", 10,
           datetime(2026, 12, 1, 10, 0), datetime(2026, 12, 1, 12, 0), "Aula 102"),
]
