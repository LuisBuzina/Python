nome = "Luis Felipe"
altura = 1.65
peso = 75.0
imc = peso / (altura ** 2) 
format_imc = "{:.2f}".format(imc) #usado para fazer limitar casas decimais
round_imc = round(imc, 2)#usado para fazer limitar casas decimais
#f-strings = forma de formatar linhas de texto
linha_1 = f'Nome= {nome}, Altura= {altura}'
linha_2 = f'Peso= {peso}, IMCf= {format_imc}, IMCr= {round_imc}, IMC= {imc:.2f}' #a variavel IMC esta formatada para deixar duas casas decimais

print(linha_1)
print(linha_2)
