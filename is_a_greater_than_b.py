def is_a_greater_than_b() -> None:
    num  = int(input('digite o primeiro numero: '))
    num2  = int(input('digite o segundo numero: '))

    if num > num2:
        print(f'''{num} > {num2}''')
    elif num < num2:
        print(f'''{num} < {num2}''')
    else:
        print(f'''{num} = {num2}''')        


is_a_greater_than_b()
