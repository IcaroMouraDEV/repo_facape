def display_greater_and_smaller():
    num1 = int(input('1° numero: '))
    num2 = int(input('2° numero: '))
    num3 = int(input('3° numero: '))
    num_arr = [num1, num2, num3]

    num_arr.sort()

    print(
        f'o menor numero é {num_arr[0]}\n'
        f'e o maior numero é {num_arr[2]}'
    )


display_greater_and_smaller()
