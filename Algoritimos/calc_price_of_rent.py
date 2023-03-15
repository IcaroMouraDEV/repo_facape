def price_of_rent() -> None:  # exibir o preço a se apagar do aluguel de um carro.
    
    days = int(input('digite quantos dias o carro foi alugado: '))
    km = float(input('digite quantos km foram pecorridos: '))
    amount = 60 * days + 0.15 * km


    print(f'''quantidade a pagar: {amount}R$''')


price_of_rent()
