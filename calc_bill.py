def calc_bill():  # calcular a conta de um telefone celular
    minutes = int(input('Digite a quantidade de minutos conversados: '))

    if minutes > 400:
        print(f'A conta a ser paga {0.15 * minutes}')
    elif minutes <= 400 and minutes >= 200:
        print(f'A conta a ser paga {0.18 * minutes}')
    else:
        print(f'A conta a ser paga {0.2 * minutes}')


calc_bill()
