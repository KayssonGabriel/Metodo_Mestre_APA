# Método Mestre

Nome: Kaysson Gabriel Inocêncio de Jesus e  Rhennan Augusto Santana do Carmo.
Tema: 1.f) Desenvolver uma ferramenta para apresentar a complexidade de tempo de algoritmos recursivos com base na aplicação do Teorema Mestre.


Entrada - O usuário envia a recorrência no formato string, seguindo o seguinte padrão:  T(n) = aT(n /b)+f(n). O f(n) será estabelecido da seguinte forma: n^k log^p n.

Primeiro passo - Normalização da expressão: A expressão é convertida para maiúsculas para evitar problemas com a diferenciação entre maiúsculas e minúsculas.
A expressão é dividida em duas partes, separadas pelo sinal de igual (=), assim ignorando a parte ‘T(n) =’, portanto, será usado somente a outra parte. Os espaços em branco são removidos de ambas as partes.

Segundo passo - identificação de Caracteres Indesejados:
Verificar se a expressão contém o caractere ‘-’, caso exista não será possível utilizar o teorema mestre para resolver a recorrência.

Terceiro passo - Verificar a presença do caractere ‘T’.
Se 'T' for encontrado, o código extrai o termo antes de ‘T’, remove qualquer parte que seja '(N/B)' e converte o termo em um número do tipo float. Caso não tenha um número acompanhando ‘T’, ‘a’ será igual a 1, ex.: T(n) = T(n/2) + n log n. Dessa forma é encontrado o termo ‘a’ do Método Mestre.

Quarto passo - Verifica-se a presença do caractere ‘N’ na expressão (primeiro ‘N’ da esquerda para direita).
Se ‘N’ for encontrado, o código tenta encontrar o termo numérico imediatamente antes de ‘N’. Esse termo é convertido em um número do tipo float. Esse passo é responsável para casos parecidos com esse exemplo: T(n) = 2T(2n/3) + n log n. Caso não encontre nenhum número antes de ‘N’, o valor será 1, pois ‘b/1’ = ‘b’ (Quinto passo).

Quinto passo - O código verifica a presença do caractere ‘/’ e ‘)’ na expressão. Se ambos forem encontrados, o código extrai o termo entre a barra e o parêntese direito ‘)’, converte-o em um número do tipo float e divide pelo valor obtido na etapa anterior (Quarto Passo: Antes do primeiro N). Dessa forma é encontrado o termo ‘b’ do Método Mestre.

Sexto passo - Verificar a presença do caractere ‘^’.
Se ‘^’ for encontrado, e o caractere antes dele é ‘N’, extrai o próximo termo de ‘^’ até o ‘log’ e converte em um número do tipo float. Dessa forma é encontrado o termo ‘k’ do Método Mestre. Se não encontrar ‘^’, verifica-se a presença do caractere ‘N’ e se o próximo for ‘log’, ‘k’ será igual a 1. Se não for encontrado ‘N’ com próximo caractere ‘log’, ‘k’ será igual a 0. Se não houver a presença do ‘log’, a verificação continuará até o final da expressão.

Sétimo passo - Verificar a presença do caractere 'log'.
Se ‘log’ for encontrado, e o caractere depois dele é ‘^’, extrai o próximo termo de ‘^’, remove o ‘N’ e converte em um número do tipo float. Dessa forma é encontrado o termo ‘p’ do Método Mestre. Se não encontrar ‘^’, ‘p’ será igual a 1. Se não for encontrado ‘log’, ‘p’ será igual a 0.

Oitavo passo - Verificar se ‘a’ >= 1, caso não, retornar ‘não é possível utilizar o método mestre, pois ‘a’ é menor que 1 ’. Verificar se ‘b’ > 1, caso não,  retornar ‘não é possível utilizar o método mestre, pois ‘b’ é menor que 1.

Nono passo - Caso seja possível utilizar o método mestre, imprimir da seguinte forma:
a = (valor obtido de a)
b = (valor obtido de b)
f(n) = (n^k log^p n)
k = (valor obtido de k)
p = (valor obtido de p)

Décimo passo -  Calcular o logaritmo utilizando math.log(), onde math.log(x, base), ou seja, math.log(a, b).

Décimo primeiro passo - Identificar em qual caso esta.
Caso 1: Se o resultado de math.log(a, b) > k, retornará: ‘Está no Caso 1: T(n) = Theta(n^log(a, b))’.
Caso 2: Se o resultado de math.log(a, b) = k.
Se p > -1, então retornará: ‘Está no Caso 2 e p > -1: T(n) = Theta(n^k log^(p+1) n)’.
Se p = -1, então retornará: ‘Está no Caso 2 e p = -1: T(n) = Theta(n^k log log n)’.
Se p < -1, então retornará: ‘Está no Caso 2 e p < -1: T(n) = Theta(n^k)

Caso 3: Se, k > math.log(a, b).
Se p >= 0, então retornará: ‘Está no Caso 3 e p >= 0 : T(n) = Theta(n^k log^p n)’.
Se p < 0, então retornará: ‘Está no Caso 3 e p < 0 : T(n) = Theta(n^k)’.
