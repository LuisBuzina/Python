import random

aluno1 = str(input('Quais os nome dos alunos para o sorteio: '))
aluno2 = str(input('Quais os nome dos alunos para o sorteio: '))
aluno3 = str(input('Quais os nome dos alunos para o sorteio: '))
aluno4 = str(input('Quais os nome dos alunos para o sorteio: '))

lista = [aluno1, aluno2, aluno3, aluno4]
#aleatorio = random.randint(1, 10) # randint aleatoriza numeros de inteiros em um range
escolido = random.choice(lista) #random.choice usado para escolher aleatorio dentro de uma variavel composta = lista
print('O aluno escolido foi: {}' .format(escolido))