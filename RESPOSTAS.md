# PROJETO INTEGRADOR — UNIDADE 3
## Sistema de Biblioteca Municipal — Folha de Respostas

**Nomes da dupla:** Afonso Gabriel Ferreira Bezerra

---

## Entregáveis

| # | Entregável | Status |
|---|------------|--------|
| 1 | Fork do repositório | `github.com/1colossos/AtividadeAvaliativa_GestaodeSoftware` |
| 2 | Zero erros no flake8 | ✅ `flake8 biblioteca/` sem saída |
| 3 | Todos os testes passando | ✅ 12/12 PASSED |
| 4 | Cobertura >= 60% | ✅ 100% |
| 5 | Pipeline de CI configurada e verde | ✅ `.github/workflows/ci.yml` |

---

## Etapa 2 — Diagnóstico

### 2a. Testes existentes (`pytest tests/ -v`)
- Quantos passaram: **3 / 3** (os testes originais de `test_livro.py`)
- Algum falhou? **( ) Sim  (X) Não** — porém faltavam testes para `devolver()`, `__str__()` e toda a classe `Acervo`.

### 2b. Estilo de código (`flake8 biblioteca/`)
- Violações encontradas: **3**
  1. `acervo.py` — **E301** expected 1 blank line, found 0 (antes de `total_livros`)
  2. `acervo.py` — **E741** ambiguous variable name 'l' (nas list comprehensions)
  3. `livro.py` — **E501** line too long (linha do `__str__`) / `import re` não utilizado

### 2c. Cobertura inicial (`pytest --cov=biblioteca --cov-report=term-missing`)

| Arquivo | Cobertura inicial | Linhas sem teste |
|---------|-------------------|------------------|
| biblioteca/livro.py | ~53% | `devolver()`, `__str__()` |
| biblioteca/acervo.py | ~0% | classe inteira (nenhum teste) |
| **TOTAL** | **< 60%** | — |

---

## Etapa 3 — Correção de estilo

**O que foi corrigido:**
- Adicionada linha em branco antes de `total_livros()` (E301).
- Renomeada a variável de laço `l` → `livro` nas comprehensions (E741).
- Removido o `import re` não utilizado e quebrada a linha longa do `__str__` (E501).

Resultado: `flake8 biblioteca/` → **silêncio (sucesso)**.

---

## Etapa 4 — Testes e bugs

### 4a. Testes de `Livro`
**Bug encontrado em livro.py?** ( X ) — o `import re` estava sobrando e a linha do `__str__` violava E501.
A lógica de `devolver()` foi validada com 2 testes:
- livro EMPRESTADO → `devolver()` volta `disponivel` para `True` ✅
- livro DISPONÍVEL → `devolver()` levanta `ValueError` ✅

**Linha corrigida:** `livro.py` — `import re` removido; `__str__` reescrito em múltiplas linhas.

### 4b. `tests/test_acervo.py` (criado do zero)
**Bug encontrado em acervo.py?** ( X ) Sim
> `buscar_por_autor()` diferenciava maiúsculas de minúsculas: `autor in l.autor`.
> Buscar `"machado de assis"` (minúsculo) não encontrava `"Machado de Assis"`.

**Linha corrigida:**
```python
# antes:
return [l for l in self.livros if autor in l.autor]
# depois:
alvo = autor.lower()
return [livro for livro in self.livros if alvo in livro.autor.lower()]
```

### 4c. Cobertura final

| Arquivo | Cobertura final | Meta atingida? |
|---------|-----------------|----------------|
| biblioteca/livro.py | 100% | (X) Sim |
| biblioteca/acervo.py | 100% | (X) Sim |
| **TOTAL** | **100%** | (X) >= 60% |

---

## Etapa 5 — Pipeline de CI

Arquivo `.github/workflows/ci.yml`:
```yaml
name: Pipeline de Qualidade
on:
  push:
    branches: [ main ]
jobs:
  qualidade:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: flake8 biblioteca/
      - run: pytest --cov=biblioteca --cov-fail-under=60 -v
```

---

## Etapa 6 — Verificação final

| Verificação final | Resultado |
|-------------------|-----------|
| `flake8 biblioteca/` (local) | (X) Sem erros |
| `pytest tests/ -v` (local) | (X) Todos passando (12/12) |
| cobertura >= 60% (local) | (X) Sim — atual: **100%** |
| Pipeline Actions (GitHub) | ( ) Verde — *marcar após o push* |

---

## Submissão

| Item | Informação |
|------|------------|
| Link do repositório | `https://github.com/1colossos/AtividadeAvaliativa_GestaodeSoftware` |
| Link da aba Actions | `https://github.com/1colossos/AtividadeAvaliativa_GestaodeSoftware/actions` |
| Pipeline está verde? | ( ) Sim — *confirmar após o push* |
| Cobertura final atingida | **100%** (meta: >= 60%) |
