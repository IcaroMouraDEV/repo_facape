def calc_energy_bill():
    kwh = int(input('Quantos kw/h foram consumidos? '))
    type = input('Qual o tipo de instalação do imovel? ')

    prices = {
        'R': [500, (0.40, 0.65)],
        'C': [1000, (0.55, 0.60)],
        'I': [5000, (0.55, 0.60)]
    }

    type = prices[type]

    if kwh <= type[0]:
        print(f'O preço de sua conta de energia é {kwh * type[1][0]}R$')
    else:
        print(f'O preço de sua conta de energia é {kwh * type[1][1]}R$')
        


calc_energy_bill()
