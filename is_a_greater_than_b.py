def is_a_greater_than_b() -> None:
    num  = int(input('digite o primeiro numero: '))
    num2  = int(input('digite o segundo numero: '))

    if num > num2:
        print(f'{num} é maior que {num2}')
    elif num < num2:
        print(f'{num} é menor que {num2}')
    else:
        print(f'{num} é igual a {num2}')        


is_a_greater_than_b()
