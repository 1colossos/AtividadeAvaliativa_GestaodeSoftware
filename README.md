# Sistema de Biblioteca Municipal — Projeto Integrador (Unidade 3)

**ITMADS537 — Gestão da Qualidade e Teste de Software | UEMA NET — Polo Itapecuru-Mirim**

Aluno: **Afonso Gabriel Ferreira Bezerra**

[![Pipeline de Qualidade](https://github.com/1colossos/AtividadeAvaliativa_GestaodeSoftware/actions/workflows/ci.yml/badge.svg)](https://github.com/1colossos/AtividadeAvaliativa_GestaodeSoftware/actions)

---

## Sobre a atividade

Sistema de gerenciamento de acervo para a Biblioteca Municipal de Itapecuru-Mirim.
O cenário do projeto é o de um **analista de qualidade júnior** que recebe o código de um
desenvolvedor sênior e precisa garantir a qualidade dele. As tarefas avaliadas foram:

1. Fazer o **fork/clone** do repositório e instalar as dependências.
2. **Diagnosticar** problemas de estilo, testes faltando e bugs.
3. **Corrigir as violações de estilo** apontadas pelo `flake8`.
4. **Escrever os testes** que faltavam e, com eles, **descobrir e corrigir os bugs**.
5. Atingir **cobertura de testes ≥ 60%**.
6. Configurar uma **pipeline de CI** no GitHub Actions que valide tudo automaticamente.

---

## Estrutura do projeto

```
AtividadeAvaliativa_GestaodeSoftware/
├── biblioteca/
│   ├── __init__.py
│   ├── livro.py          # classe Livro: título, autor, ISBN, disponibilidade
│   └── acervo.py         # classe Acervo: coleção de livros (busca, empréstimo, devolução)
├── tests/
│   ├── __init__.py
│   ├── test_livro.py     # testes da classe Livro (completados)
│   └── test_acervo.py    # testes da classe Acervo (criados do zero)
├── .github/workflows/
│   └── ci.yml            # pipeline de CI (flake8 + pytest com cobertura)
├── requirements.txt      # pytest, pytest-cov, flake8
├── RESPOSTAS.md          # folha de respostas preenchida da atividade
└── README.md
```

### As classes

- **`Livro`** — representa um livro. Métodos: `emprestar()`, `devolver()` e `__str__()`.
  Um livro nasce disponível (`disponivel = True`); ao ser emprestado fica indisponível e,
  ao ser devolvido, volta a ficar disponível. Tentativas inválidas levantam `ValueError`.
- **`Acervo`** — gerencia uma lista de `Livro`. Métodos: `adicionar_livro()`,
  `total_livros()`, `buscar_por_titulo()`, `buscar_por_autor()`, `livros_disponiveis()`
  e `livros_emprestados()`.

---

## Como executar

Instale as dependências (de preferência em um ambiente virtual):

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Comandos de verificação:

```bash
pytest tests/ -v                                    # roda os testes
pytest --cov=biblioteca --cov-report=term-missing   # relatório de cobertura
pytest --cov=biblioteca --cov-fail-under=60         # falha se cobertura < 60%
flake8 biblioteca/                                  # verifica o estilo (silêncio = ok)
```

---

## O que foi feito

### 1. Correções de estilo (flake8)

| Arquivo | Código | Problema | Correção |
|---------|--------|----------|----------|
| `acervo.py` | **E301** | Faltava linha em branco antes de `total_livros()` | Linha em branco adicionada |
| `acervo.py` | **E741** | Variável de laço `l` é ambígua | Renomeada para `livro` |
| `livro.py`  | —      | `import re` não utilizado | Import removido |
| `livro.py`  | **E501** | Linha do `__str__` com mais de 79 caracteres | Quebrada em múltiplas linhas |

Resultado: `flake8 biblioteca/` não retorna nenhuma saída.

### 2. Bug de lógica corrigido (`acervo.py`)

O método `buscar_por_autor()` diferenciava maiúsculas de minúsculas, então buscar
`"machado de assis"` não encontrava `"Machado de Assis"`:

```python
# antes (com bug)
return [l for l in self.livros if autor in l.autor]

# depois (corrigido)
alvo = autor.lower()
return [livro for livro in self.livros if alvo in livro.autor.lower()]
```

A busca por título já era case-insensitive e foi coberta por testes para garantir isso.

### 3. Testes escritos

- **`tests/test_livro.py`** (completado): devolução de livro emprestado, devolução de
  livro já disponível (deve levantar `ValueError`) e o formato do `__str__` nos dois
  estados (disponível/emprestado).
- **`tests/test_acervo.py`** (novo): adição de livros e contagem, busca por título
  (parcial e case-insensitive), busca por autor (case-insensitive) e as listas de
  livros disponíveis/emprestados após um empréstimo.

**Cobertura final: 100%** (meta era ≥ 60%).

```
Name                     Stmts   Miss  Cover
------------------------------------------------
biblioteca/__init__.py       0      0   100%
biblioteca/acervo.py        18      0   100%
biblioteca/livro.py         17      0   100%
------------------------------------------------
TOTAL                       35      0   100%
```

### 4. Pipeline de CI (GitHub Actions)

O arquivo `.github/workflows/ci.yml` roda a cada `push` na branch `main`:

- Baixa o código (`actions/checkout`);
- Configura o Python 3.11 (`actions/setup-python`);
- Instala as dependências;
- Roda `flake8 biblioteca/`;
- Roda `pytest` exigindo cobertura mínima de 60%.

A pipeline pode ser acompanhada na aba
[**Actions**](https://github.com/1colossos/AtividadeAvaliativa_GestaodeSoftware/actions).

---

## Resumo dos entregáveis

| # | Entregável | Status |
|---|------------|--------|
| 1 | Repositório no GitHub | ✅ |
| 2 | Zero erros no flake8 | ✅ |
| 3 | Todos os testes passando | ✅ 12/12 |
| 4 | Cobertura ≥ 60% | ✅ 100% |
| 5 | Pipeline de CI verde | ✅ |

> Projeto para fins educacionais. UEMA NET — Polo Itapecuru-Mirim.
