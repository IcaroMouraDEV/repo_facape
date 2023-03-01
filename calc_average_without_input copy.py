def average() -> None:  # Calcular a média

    nota1 = int(input('Digite a 1° nota: '))
    nota2 = int(input('Digite a 2° nota: '))
    nota3 = int(input('Digite a 3° nota: '))
    nota4 = int(input('Digite a 4° nota: '))
    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media >= 7:
        print('Aprovado')
    else:
        print('Reprovado')


average()
