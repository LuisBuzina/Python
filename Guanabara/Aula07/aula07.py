n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

soma = n1 + n2
subtracao = n1 - n2
multil = n1 * n2
divisao = n1 / n2
divinteira = n1 // n2
potencia = n1 ** n2
restodiv = n1 % n2

print('Os resultados da soma: {} subtração: {} multiplicação: {}'.format(soma, subtracao, multil), end=' ++++ ')
print('divisão: {:.3f} divisão inteira: {} potencia: {} resto divisao: {}'.format(divisao, divinteira, potencia, restodiv))