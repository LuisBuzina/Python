import math
numero_a = input("Digite o primeiro numero: ")
numero_b = input("Digite o segundo numero: ")
numero_c = input("Digite o terceiro numero: ")

i_numero_a = int(numero_a)
i_numero_b = int(numero_b)
i_numero_c = int(numero_c)

delta = i_numero_b**2 - 4*i_numero_a*i_numero_c
raiz_quad = math.sqrt(delta)

encontre_x_positivo = (-i_numero_b + raiz_quad)/(2*i_numero_a)
encontre_x_positivo = "{:.2f}".format(encontre_x_positivo)

encontre_x_negativo = (-i_numero_b - raiz_quad)/(2*i_numero_a)
encontre_x_negativo = "{:.2f}".format(encontre_x_negativo)

print(delta)
print(encontre_x_positivo)
print(encontre_x_negativo)
