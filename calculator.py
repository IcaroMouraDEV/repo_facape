def calculator():
    print(f'''
Escolha qual operação vai querer das seguintes opções:
    soma
    subtração
    multiplicação
    divisão
    ''')
    num1 = int(input('Qual o 1° numero: '))
    num2 = int(input('Qual o 2° numero: '))
    operator = input('Qual a operação: ')
    operators = {
        'soma': num1 + num2,
        'subtração': num1 - num2,
        'multiplicação': num1 * num2,
        'divisão': num1 / num2
    }

    print(f'o resultado da {operator} é {operators[operator]}')


calculator()
