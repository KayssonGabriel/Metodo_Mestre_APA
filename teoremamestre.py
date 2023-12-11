import math
import re


_NUMERO = r'(?:[0-9]+(?:\.[0-9]+)?|\.[0-9]+)'
_EXPOENTE = rf'[+-]?{_NUMERO}'
_RECORRENCIA = re.compile(
    rf'T\(N\)=(?P<a>{_NUMERO})?T\((?P<escala>{_NUMERO})?N/'
    rf'(?P<divisor>{_NUMERO})\)\+(?P<termo>.+)'
)
_TERMO = re.compile(
    rf'(?:(?P<constante>{_NUMERO})|'
    rf'(?:N(?:\^(?P<k>{_EXPOENTE}))?)(?:LOG(?:\^(?P<p_com_n>{_EXPOENTE}))?N)?|'
    rf'LOG(?:\^(?P<p_sem_n>{_EXPOENTE}))?N)'
)


class Teorema:

    @staticmethod
    def removeSpaces(expressionVect):
        return [char for char in expressionVect if not char.isspace()]

    @staticmethod
    def metodo_mestre(expression):
        normalizada = ''.join(Teorema.removeSpaces(expression.upper()))
        recorrencia = _RECORRENCIA.fullmatch(normalizada)
        termo = _TERMO.fullmatch(recorrencia['termo']) if recorrencia else None
        if termo is None:
            print("Formato inválido. Use T(n) = aT(n/b) + n^k log^p n.")
            return

        a = float(recorrencia['a'] or 1)
        escala = float(recorrencia['escala'] or 1)
        divisor = float(recorrencia['divisor'])
        constante = float(termo['constante'] or 1)
        k = float(termo['k'] or (1 if recorrencia['termo'].startswith('N') else 0))
        p = float(termo['p_com_n'] or termo['p_sem_n'] or (1 if 'LOG' in recorrencia['termo'] else 0))
        if not all(math.isfinite(valor) for valor in (a, escala, divisor, constante, k, p)):
            print("Use somente parâmetros numéricos finitos.")
            return
        if escala <= 0 or constante <= 0:
            print("O argumento recursivo e o termo adicional devem ser positivos.")
            return

        b = divisor / escala
        if a < 1 or b <= 1 or not math.isfinite(b):
            print("Não é possível utilizar o método mestre: a deve ser ≥ 1 e b > 1.")
            return

        print(f"a = {a:g}")
        print(f"b = {b:g}")
        print(f"f(n) = n^{k:g} log^{p:g} n")

        log_a = math.log(a, b)
        if math.isclose(log_a, k, rel_tol=1e-12, abs_tol=1e-12):
            if p > -1:
                resultado = f"n^{k:g} log^{p + 1:g} n"
            elif p == -1:
                resultado = f"n^{k:g} log log n"
            else:
                resultado = f"n^{k:g}"
            print(f"Está no Caso 2: T(n) = Theta({resultado})")
        elif log_a > k:
            print(f"Está no Caso 1: T(n) = Theta(n^{log_a:g})")
        else:
            print(f"Está no Caso 3: T(n) = Theta(n^{k:g} log^{p:g} n)")
