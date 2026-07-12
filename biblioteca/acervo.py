class Acervo:
    """Gerencia o conjunto de livros de uma biblioteca."""

    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        """Adiciona um livro ao acervo."""
        self.livros.append(livro)

    def total_livros(self):
        """Retorna o total de livros no acervo."""
        return len(self.livros)

    def buscar_por_titulo(self, titulo):
        """Busca pelo titulo (sem diferenciar maiusculas/minusculas)."""
        alvo = titulo.lower()
        return [livro for livro in self.livros if alvo in livro.titulo.lower()]

    def buscar_por_autor(self, autor):
        """Busca pelo autor (sem diferenciar maiusculas/minusculas)."""
        alvo = autor.lower()
        return [livro for livro in self.livros if alvo in livro.autor.lower()]

    def livros_disponiveis(self):
        """Retorna lista de livros disponiveis para emprestimo."""
        return [livro for livro in self.livros if livro.disponivel]

    def livros_emprestados(self):
        """Retorna lista de livros atualmente emprestados."""
        return [livro for livro in self.livros if not livro.disponivel]
