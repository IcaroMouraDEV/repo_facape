def display_multiplication_table():
    num = int(input('Digite um número para calcular a tabuada: '))
    index = 0
    while index <= 10:
        print(f'{index}x{num} = {index * num}')
        index += 1


display_multiplication_table()
