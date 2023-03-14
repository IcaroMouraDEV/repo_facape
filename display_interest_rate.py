def display_interest_rate():
    funds = float(input('Digite o depósito inicial: '))
    interest_rate = float(input('Digite o juros anual: '))
    interest_rate = (interest_rate / 100) / 12
    index = 1
    while index <= 12:
        print(
            f'{index}° mês, o rendimento de {funds}R$ foi '
            f'{funds * (interest_rate)}R$'
        )
        funds += funds * (interest_rate)
        index += 1


display_interest_rate()
