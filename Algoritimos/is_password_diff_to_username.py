def is_password_diff_to_username():
    print('sua senha não pode ser igual ao seu nome')
    name = input('digite seu nome: ')
    password = input('digite sua senha: ')

    while name == password:
        password = input('digite sua senha, diferente do seu nome: ')

    print('Usuario cadastrado com sucesso 👍')

is_password_diff_to_username()
