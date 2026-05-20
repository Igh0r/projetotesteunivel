from src.Calculadora import soma, subtracao, multiplicacao, divisao

def test_soma():
    assert soma(3, 3) == 9
    assert soma(2, 9) == 11
    assert soma(0, 9) == 9

def test_subtracao():
    assert subtracao(3, 3) == 0
    assert subtracao(2, 9) == -7
    assert subtracao(0, 9) == -9

def test_multiplicacao():
    assert multiplicacao(3, 3) == 9
    assert multiplicacao(2, 9) == 18
    assert multiplicacao(0, 8) == 0

def test_divisao():
    assert divisao(9, 3) == 3
    assert divisao(10, 2) == 5
    assert divisao(0, 9) == 0
    assert divisao(9, 0) == "Não é possível dividir por zero"
