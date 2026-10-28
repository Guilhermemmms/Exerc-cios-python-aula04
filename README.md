# Exercícios de Python: Aula 4 (Estruturas Condicionais)

Exercícios da disciplina **Computational Logic Using Python** (UniFECAF), sobre
estruturas de decisão em Python: `if` / `elif` / `else`, operadores de
comparação e operadores lógicos (`and`, `or`, `not`).

## Exercícios

| # | Arquivo | Nível | Conceito principal |
|---|---------|-------|--------------------|
| 01 | `ex01_verificador_numero.py` | Fácil | `if / elif / else` com operadores de comparação |
| 02 | `ex02_par_ou_impar.py` | Fácil | Operador módulo (`%`) e blocos de decisão independentes |
| 03 | `ex03_classificador_desconto.py` | Médio | Faixas em cadeia `elif` + regra cumulativa em `if` separado |
| 04 | `ex04_classificacao_desempenho.py` | Médio | `and` / `or` e ordem das condições |
| 05 | `ex05_validador_login.py` | Médio | Comparação de strings com `and` |
| 06 | `ex06_desconto_por_perfil.py` | Médio | Regras ordenadas, `.lower()` e valores booleanos |
| 07 | `ex07_sistema_beneficios.py` | Difícil | `and` + `or` combinados, uso de parênteses |
| 08 | `ex08_entrada_evento.py` | Difícil | Condições de "veto" primeiro, uso de `not` |
| 09 | `ex09_notas_situacao.py` | Difícil | Média, validação de entrada com `while` e função |
| 10 | `ex10_calculadora_imposto.py` | Difícil | Tabela de faixas, fórmula com parcela a deduzir, `f-strings` |

## Como executar

Requer Python 3.8 ou superior.

```bash
python ex01_verificador_numero.py
```

Troque o nome do arquivo para executar outro exercício. Cada programa pede os
dados pelo teclado e mostra o resultado no terminal.

## O que aprendi

- O Python executa só o **primeiro** bloco verdadeiro de uma cadeia
  `if / elif`, então a **ordem** das condições muda o resultado.
- Regras mutuamente exclusivas usam `elif`; regras cumulativas usam `if`
  separados.
- Em faixas que se sobrepõem, testo da condição mais restritiva para a mais
  ampla.
- Ao misturar `and` e `or`, uso parênteses para deixar a intenção explícita.

## Observações sobre os enunciados

Ao conferir os exemplos dos enunciados com as regras escritas, encontrei duas
inconsistências, comentadas nos próprios arquivos:

- **Exercício 04:** o exemplo "nota 5,0 / frequência 70" indica *Insuficiente*,
  mas a regra "nota ≥ 5 **ou** frequência ≥ 75" resulta em *Regular*.
- **Exercício 10:** o exemplo de salário R$ 2.500,00 mostra imposto de 17,06,
  mas o cálculo `2500 × 0,075 − 169,44` resulta em 18,06.
