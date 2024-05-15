from math import pow #potencia elevadoa alguma coisa
from math import sqrt #raiz quadrada

oposoto = float(input('Escreva o cateto oposto: '))
adjacente = float(input('Escreva o cateto adjacente: '))

valor1 = pow(oposoto, 2)
valor2 = pow(adjacente, 2)
hipotenusa = sqrt((pow(oposoto, 2)) + (pow(adjacente, 2)))

print('A hipotenusa é: {:.2f}' .format(hipotenusa))