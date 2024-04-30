multiplo = int(input('Digite o valor para a tabuada: '))

i = 0

while i <= 10 :
    resultado = multiplo * i
    print('{} x {} = {}' .format(multiplo, i, resultado))
    i += 1