dias = int(input('Quantos dias o carro foi usado: '))
km = float(input('Quantos kilometros foram percorridos: '))

diasCusto = float(dias * 60)
kmCusto = float(km * 0.15)

print('O dias usados foram: {} os kilometros rodados foram: {}. \nE o total de custo foi: {}'.format(dias, km, (diasCusto + kmCusto)))