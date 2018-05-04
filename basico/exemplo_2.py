"""Base para testes."""
from unittest import TestCase, main


def add(x, y):
    """Função de adição, soma dois valores."""
    return x + y


# assert add(7, 7) == 15, 'o valor da soma está errado.'

# pytest

class TestAdd(TestCase):
    def test_soma_deve_retornar_14(self):
        entrada = add(7, 7)
        esperado = 15
        self.assertEqual(entrada, esperado)

main()
