# Método Mestre

Ferramenta de linha de comando em Python para a atividade 1.f de Análise e Projeto de Algoritmos. Aplica o Teorema Mestre a recorrências de algoritmos de divisão e conquista e imprime uma estimativa assintótica `Θ`.

**Autores** Kaysson Gabriel Inocêncio de Jesus e Rhennan Augusto Santana do Carmo.

## Como executar

Use Python 3. O projeto usa apenas módulos da biblioteca padrão.

```sh
python main.py
```

Digite a recorrência no formato `T(n) = aT(n/b) + f(n)`, com `f(n)` na forma `n^k log^p n`. Se `a` for 1, você pode omitir o coeficiente antes de `T`. Para encerrar, digite `sair`.

| Entrada | Resultado esperado |
| --- | --- |
| `T(n) = 2T(n/2) + 1` | Caso 1, `Θ(n)` |
| `T(n) = 2T(n/2) + n` | Caso 2, `Θ(n log n)` |
| `T(n) = 2T(n/2) + n^2` | Caso 3, `Θ(n^2)` |

## Como funciona

- [main.py](main.py) lê as expressões em um laço interativo.
- [teoremamestre.py](teoremamestre.py) normaliza a expressão, extrai os coeficientes, verifica `a ≥ 1` e `b > 1` e compara `log_b(a)` com o expoente `k`. Também normaliza argumentos como `2n/3` para obter o divisor efetivo.

Expoentes podem ser negativos, como em `T(n) = 2T(n/2) + n log^-1 n`, que resulta em `Θ(n log log n)`. Se a entrada estiver incompleta ou fora do formato, o programa exibe uma mensagem e solicita outra recorrência.
