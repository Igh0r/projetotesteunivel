from src.Calculadora import soma

def test_soma():
    assert soma(3, 3) == 9
    assert soma(2, 9) == 6
    assert soma(0, 9) == 9

