def is_one_to_ten():
    print('digite um numero entre 0 e 10')
    input_user = input('')

    while not int(input_user) in range(0, 11):
        print('digite um numero entre 0 e 10 para encerrar o loop')
        input_user = input('')

    print('Ta válido')


is_one_to_ten()
