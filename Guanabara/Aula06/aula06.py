n1 = int (input('Digite um valor: '))
n2 = int(input ('Digite outro valor: '))

res = n1 + n2

print('O resultado é {}'.format(res)) #formas simples de print
print('O resultado entre', n1, '+', n2,': {}'.format(res)) #forma que mostra quais numeros foram usados para somar
print('O resultado entre {} + {} = {}'.format(n1, n2, res)) #forma de não precisar ficar abrindo e fechando aspas usando {}
