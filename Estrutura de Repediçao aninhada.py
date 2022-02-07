while True:
    s1 = int(input('Qual sua idade '))
    if s1 < 0:
        print('encerrado')
        break
    s2 = input('Qual seu sexo "M" "F" ')
    if s2 == "M" or s2 == "m":
     print('Boa noite senhor sua idade {}anos '.format(s1))
    if s2 == "F" or s2 == "f":
     print('Boa noite senhora sua idade {}anos '.format(s1))
     break
    else:
        print('Opção de sexo inexistente')






















