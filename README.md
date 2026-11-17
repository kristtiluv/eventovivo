# EventoVivo

Aplicación para gestionar talleres, hackatones y encuentros universitarios: agenda de sesiones, inscripción con validación de cupo y choques de horario, lista de espera y asistencia con código QR.

Proyecto de Modelado Ágil de Software (ULEAM, 2026-2). Todos los datos son ficticios.

## Integrantes
- Mikaela Bailón
- Alexis Lucas
- Kristin Morales
- Yomaira Valarezo

## Requisitos
- Python 3.10 o superior
- pip

## Cómo ejecutar

```bash
git clone https://github.com/kristtiluv/eventovivo.git
cd eventovivo
python -m venv .venv
source .venv/bin/activate      # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Cómo correr las pruebas

```bash
python -m pytest
```

## Estrategia de ramas
- `main`: rama estable. Solo recibe código que ya pasó pruebas y revisión.
- Una rama por historia, con el ID en el nombre. Ejemplo: `feature/HU-01-agenda`.
- Cada rama se une a `main` con un pull request, revisado por una compañera antes de aceptarlo.

## Enlaces
- Tablero Kanban: [pegar enlace]
- Plan de planificación ágil: https://docs.google.com/document/d/1met2NxWbBhTYC9894s30nfDU31PO0Kww3q4lek4cMlk/edit?usp=sharing
