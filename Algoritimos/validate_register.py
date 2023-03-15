def validate_register():
    config = {
        'nome_length': {'min': 3},
        'age': {'min': 0, 'max': 150},
        'salary': {'min': 1},
        'gender': ['f', 'm'],
        'status': ['s', 'c', 'v', 'd']
    }
    try:
        name = input('Digite seu nome: ')
        age = input('Digite sua idade: ')
        salary = float(input('Digite seu salário: '))
        print('Digite seu genero, [m] Masculino, [f] Feminino')
        gender = input('')
        print('Digite seu genero, [m] Masculino, [f] Feminino')
        age = input('Digite sua idade: ')
    except ValueError:
        print('Salario e Idade tem que ser um número')
