n = input('Digite algo: ')

print ('Alfabetico= ', n.isalpha()) #alfabetico True= aa fd fr False= 3d 45 (espaço vazio)
print ('Alfabetico (format)= {}'.format(n.isalpha())) #alfabetico True= aa fd fr False= 3d 45 (espaço vazio)
print ('Numerico= ', n.isnumeric()) #numerico True= 3 3.5 -43 False= aa 3d (espaço vazio)
print ('Numerico (format)= {}'.format(n.isnumeric())) #numerico True= 3 3.5 -43 False= aa 3d (espaço vazio)
print ('Alfanumerico= ', n.isalnum()) #alfanumerico True= 1 3d aaa False= (espaço vazio)
print ('Alfanumerico (format)= {}'.format(n.isalnum())) #alfanumerico True= 1 3d aaa False= (espaço vazio)
print ('Maiuscula= ', n.isupper()) #tudo em maiuscula True= AAAAA False= Sa as aP
print ('Maiuscula (format)= {}'.format(n.isupper())) #tudo em maiuscula True= AAAAA False= Sa as aP
print ('Minuscula= ', n.islower()) #tudo minusculo True= assd False= Sa DS aP
print ('Minuscula (format)= {}'.format(n.islower())) #tudo minusculo True= assd False= Sa DS aP
print ('Espaço= ', n.isspace()) #se tem espaço True= (espaço vazio) False= Sa DS aP
print ('Espaço (format)= {}'.format(n.isspace())) #se tem espaço True= (espaço vazio) False= Sa DS aP
print ('Capitalizada= ', n.istitle()) #se a primeira letra maiusculas e minusculas True= Sa False= as aP AA
print ('Capitalizada (format)= {}'.format(n.istitle())) #se a primeira letra maiusculas e minusculas True= Sa False= as aP AA