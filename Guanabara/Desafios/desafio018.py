import math

angulo = float(input('Escreva o um angulo pra calcular: '))

# Ângulo em radianos
radianos = math.radians(angulo)

# Seno
seno = math.sin(radianos)

# Cosseno
cosseno = math.cos(radianos)

# Tangente
tangente = math.tan(radianos)

# Exibindo os resultados
print("Seno: {:.3}" .format(seno))
print("Cosseno: {:.3}" .format(cosseno))
print("Tangente: {:.3}" .format(tangente))
