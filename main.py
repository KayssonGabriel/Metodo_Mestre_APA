from teoremamestre import Teorema

if __name__ == '__main__':
    teorema_instance = Teorema()
    while True:
        print()
        print("________________________________________________________________________________")
        print("Digite a Recorrência que se deseja analisar ou 'sair' para encerrar o programa.")
        print("T(n) = aT(n /b)+f(n). O f(n) será estabelecido da seguinte forma: n^k log^p n")
        
        try:
            expression = input()
        except EOFError:
            break
        if expression.strip().lower() == 'sair':
            break 
        else:
            teorema_instance.metodo_mestre(expression)
        
