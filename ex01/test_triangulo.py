from Triangulo import Triangulo
import pytest

# Testes para valores válidos
@pytest.mark.parametrize(
    "lado_a, lado_b, lado_c, resultado_esperado",
    [
        (100, 100, 100, "Equilátero"),
        (5, 5, 3, "Isósceles"),
        (7, 10, 5, "Escaleno"),
        (199, 100, 100, "Isósceles"),
        (100, 199, 100, "Isósceles"),
        (100, 100, 1, "Isósceles"),
        (1, 1, 1, "Equilátero"),
        (1, 2, 2, "Isósceles"),
        (1, 100, 100, "Isósceles"),
        (2, 2, 1, "Isósceles"),
        (2, 2, 2, "Equilátero"),
        (2, 100, 100, "Isósceles"),
        (2, 199, 199, "Isósceles"),
        (2, 200, 199, "Escaleno"),
        (2, 200, 200, "Isósceles"),
        (100, 100, 1, "Isósceles"),
        (100, 100, 2, "Isósceles"),
        (100, 100, 100, "Equilátero"),
        (100, 100, 199, "Isósceles"),
        (100, 199, 199, "Isósceles"),
        (100, 199, 200, "Escaleno"),
        (100, 200, 199, "Escaleno"),
        (199, 1, 199, "Isósceles"),
        (199, 2, 199, "Isósceles"),
        (199, 100, 100, "Isósceles"),
        (199, 2, 200, "Escaleno")
    ]
)
def test_classifica_triangulo_valido(lado_a, lado_b, lado_c, resultado_esperado):
    triangulo = Triangulo(lado_a, lado_b, lado_c)
    assert triangulo.tipo_triangulo() == resultado_esperado

# Testes para valores inválidos
@pytest.mark.parametrize(
    "lado_a, lado_b, lado_c, resultado_esperado",
    [
        (1, 1, 2, "Não é um triângulo"),
        (1, 1, 100, "Não é um triângulo"),
        (1, 1, 199, "Não é um triângulo"),
        (1, 1, 200, "Não é um triângulo"),
        (1, 2, 100, "Não é um triângulo"),
        (1, 2, 199, "Não é um triângulo"),
        (1, 2, 200, "Não é um triângulo"),
        (1, 100, 2, "Não é um triângulo"),
        (1, 100, 199, "Não é um triângulo"),
        (1, 100, 200, "Não é um triângulo"),
        (1, 199, 2, "Não é um triângulo"),
        (1, 199, 100, "Não é um triângulo"),
        (1, 199, 200, "Não é um triângulo"),
        (1, 200, 2, "Não é um triângulo"),
        (1, 200, 100, "Não é um triângulo"),
        (1, 200, 199, "Não é um triângulo"),
        (2, 1, 100, "Não é um triângulo"),
        (2, 1, 199, "Não é um triângulo"),
        (2, 1, 200, "Não é um triângulo"),
        (2, 100, 1, "Não é um triângulo"),
        (2, 100, 2, "Não é um triângulo"),
        (2, 100, 199, "Não é um triângulo"),
        (2, 199, 1, "Não é um triângulo"),
        (2, 199, 2, "Não é um triângulo"),
        (2, 199, 100, "Não é um triângulo"),
        (2, 200, 1, "Não é um triângulo"),
        (2, 200, 2, "Não é um triângulo"),
        (2, 200, 100, "Não é um triângulo"),
        (100, 1, 2, "Não é um triângulo"),
        (100, 1, 199, "Não é um triângulo"),
        (100, 1, 200, "Não é um triângulo"),
        (100, 2, 1, "Não é um triângulo"),
        (100, 2, 199, "Não é um triângulo"),
        (100, 2, 200, "Não é um triângulo"),
        (100, 199, 1, "Não é um triângulo"),
        (100, 199, 2, "Não é um triângulo"),
        (199, 1, 1, "Não é um triângulo"),
        (199, 1, 2, "Não é um triângulo"),
        (199, 1, 100, "Não é um triângulo"),
        (199, 1, 200, "Não é um triângulo"),
        (199, 2, 1, "Não é um triângulo"),
        (199, 2, 2, "Não é um triângulo"),
        (199, 2, 100, "Não é um triângulo"),
        (199, 100, 1, "Não é um triângulo"),
        (199, 100, 2, "Não é um triângulo")
    ]
)
def test_classifica_triangulo_invalido(lado_a, lado_b, lado_c, resultado_esperado):
    triangulo = Triangulo(lado_a, lado_b, lado_c)
    assert triangulo.tipo_triangulo() == resultado_esperado
