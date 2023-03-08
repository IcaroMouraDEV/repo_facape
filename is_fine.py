def is_fine() -> None:  # exibir na tela se o carro foi multado, se sim, quanto
    speed = int(input('Qual a velocidade do carro'))

    if speed > 80:
        print(
            f'você foi multado, pague {(speed - 80) * 5}'
        )


is_fine()
