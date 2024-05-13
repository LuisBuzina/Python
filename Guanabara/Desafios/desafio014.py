tempc = float(input('Qual a temperatura que você quer converter: '))

tempf = (tempc * 1.8) + 32
#tempf = ((tempc *9) / 5) + 32 # conversão completa
tempk = (tempc + 273.15)

print ('A temperatura em Celcius era de {:.2f}º convertida em Fahrenheit é de: {:.2f}º \ne a temperatura em Kelvin: {:.2f}º' .format(tempc, tempf, tempk))