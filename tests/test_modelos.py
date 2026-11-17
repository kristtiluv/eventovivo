from eventovivo.datos import SESIONES


def test_las_sesiones_ficticias_tienen_cupo_positivo():
    assert all(s.cupo > 0 for s in SESIONES)
