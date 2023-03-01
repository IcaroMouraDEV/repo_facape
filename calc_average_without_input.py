def average_without_input() -> None:  # Calcular a media sem usar input

    nota1 = 8
    nota2 = 4
    nota3 = 8
    nota4 = 10
    media = (nota1 + nota2 + nota3 + nota4) / 4

    print(media)
    # print(not True)

    if media >= 7:
        print('Aprovado')
    else:
        print('Reprovado')


average_without_input()
