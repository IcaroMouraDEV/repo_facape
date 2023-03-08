def calc_travel_price():
    km = float(input('Informe a quantidade de km da viagem: '))

    if km < 200:
        print(f'O preço da passagem é {km * 0.5}R$')
    else:
        print(f'O preço da passagem é {km * 0.45}R$')
        

calc_travel_price()
