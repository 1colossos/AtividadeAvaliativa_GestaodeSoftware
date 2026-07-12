import pytest
from biblioteca.acervo import Acervo
from biblioteca.livro import Livro


@pytest.fixture
def acervo():
    """Acervo com tres livros para os testes."""
    a = Acervo("Biblioteca Municipal de Itapecuru-Mirim")
    a.adicionar_livro(Livro("Dom Casmurro", "Machado de Assis", "111"))
    a.adicionar_livro(Livro("Memorias Postumas", "Machado de Assis", "222"))
    a.adicionar_livro(Livro("O Guarani", "Jose de Alencar", "333"))
    return a


def test_adicionar_livro_aumenta_total():
    a = Acervo("Teste")
    assert a.total_livros() == 0
    a.adicionar_livro(Livro("Livro A", "Autor A", "001"))
    assert a.total_livros() == 1
    a.adicionar_livro(Livro("Livro B", "Autor B", "002"))
    assert a.total_livros() == 2


def test_buscar_por_titulo_parcial(acervo):
    resultado = acervo.buscar_por_titulo("Dom")
    assert len(resultado) == 1
    assert resultado[0].titulo == "Dom Casmurro"


def test_buscar_por_titulo_case_insensitive(acervo):
    """Busca por titulo nao deve diferenciar maiusculas/minusculas."""
    resultado = acervo.buscar_por_titulo("dom casmurro")
    assert len(resultado) == 1
    assert resultado[0].titulo == "Dom Casmurro"


def test_buscar_por_autor_case_insensitive(acervo):
    """Busca por autor nao deve diferenciar maiusculas/minusculas."""
    resultado = acervo.buscar_por_autor("machado de assis")
    assert len(resultado) == 2
    resultado_maiusculo = acervo.buscar_por_autor("MACHADO DE ASSIS")
    assert len(resultado_maiusculo) == 2


def test_livros_disponiveis_e_emprestados(acervo):
    assert len(acervo.livros_disponiveis()) == 3
    assert len(acervo.livros_emprestados()) == 0

    acervo.livros[0].emprestar()

    assert len(acervo.livros_disponiveis()) == 2
    assert len(acervo.livros_emprestados()) == 1
    assert acervo.livros_emprestados()[0].titulo == "Dom Casmurro"
