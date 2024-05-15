from math import sqrt, floor # para importar apenas sqrt (raiz quadrada)
#import math # serve para importar toda a biblioteca
num = int(input('Digite um numero: '))

#raiz = math.sqrt(num) #sqrt serve para tirar raiz quadrada
raiz = sqrt(num) #importando direto não precisa usar referencia math. do metodo, podendo colocar apenas a função direto

print('A raiz quadrada de {0} é: {1:.2f}' .format(num, raiz))