import pytest
from biblioteca.livro import Livro


# -- Testes existentes ---------------------------------------------------

def test_criar_livro():
    livro = Livro("Dom Casmurro", "Machado de Assis", "978-85-359-0277-5")
    assert livro.titulo == "Dom Casmurro"
    assert livro.autor == "Machado de Assis"
    assert livro.disponivel is True


def test_emprestar_livro_disponivel():
    livro = Livro("O Cortico", "Azevedo", "978-85-001-0001-1")
    livro.emprestar()
    assert livro.disponivel is False


def test_emprestar_livro_ja_emprestado_levanta_erro():
    livro = Livro("Memorias Postumas", "Machado de Assis", "978-85-001-0002-2")
    livro.emprestar()
    with pytest.raises(ValueError):
        livro.emprestar()


# -- Testes adicionados --------------------------------------------------

def test_devolver_livro_emprestado():
    """Um livro emprestado deve poder ser devolvido (volta a disponivel)."""
    livro = Livro("Iracema", "Jose de Alencar", "978-85-001-0003-3")
    livro.emprestar()
    assert livro.disponivel is False
    livro.devolver()
    assert livro.disponivel is True


def test_devolver_livro_disponivel_levanta_erro():
    """Devolver um livro que ja esta disponivel deve levantar ValueError."""
    livro = Livro("Senhora", "Jose de Alencar", "978-85-001-0004-4")
    with pytest.raises(ValueError):
        livro.devolver()


def test_str_livro_disponivel():
    livro = Livro("Capitaes da Areia", "Jorge Amado", "978-85-001-0005-5")
    texto = str(livro)
    assert "Capitaes da Areia" in texto
    assert "Jorge Amado" in texto
    assert "978-85-001-0005-5" in texto
    assert "Disponivel" in texto


def test_str_livro_emprestado():
    livro = Livro("Gabriela", "Jorge Amado", "978-85-001-0006-6")
    livro.emprestar()
    assert "Emprestado" in str(livro)
