def is_new():  # exibir na tela se o carro é velho ou novo
    age: int(input('Digite a idade do carro: '))

    if age <= 3:
        print('O carro é novo')
    else:
        print('O carro é velho')


is_new()
