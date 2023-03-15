def calculator():  # Calculadora
    print('Escolha qual operação vai querer das seguintes opções:\n'
    ' soma\n'
    ' subtração\n'
    ' multiplicação\n'
    ' divisão\n'
    )
    try:
        num1 = int(input('Qual o 1° numero: '))
        num2 = int(input('Qual o 2° numero: '))
        operator = input('Qual a operação: ')
        operators = {
            'soma': num1 + num2,
            'subtração': num1 - num2,
            'multiplicação': num1 * num2,
            'divisão': num1 / num2
        }
    except ValueError:
        print('Numero inválido, digite um número corretamente.')

    try:
        print(f'o resultado da {operator} é {operators[operator]}')
    except KeyError:
        print('DIGITA UMA OPERAÇÃO CERTA ANIMAL')


calculator()
