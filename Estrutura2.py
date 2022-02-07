idade = int(input('Qual sua idade:'))
while idade > 0:

    sexo = input('Qual seu sexo: "M" "F" ')
    if sexo == "M" or sexo == "m":

        print('Boa noite senhor sua idade e {}'.format(idade))
    else:
        if sexo == "F" or sexo == 'f':
          print('Boa noite senhora sua idade e {}'.format(idade))
        else:
          print('Opção de sexo inexistente')
    idade = int(input('Qual sua idade:'))

print('encerrando programa')



