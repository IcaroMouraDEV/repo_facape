def calc_loan():
    house_price = int(input('Qual o valor da casa? '))
    client_salary = int(input('Qual o seu salário? '))
    years = int(input('Vai pagar durante quantos anos? '))
    installment = house_price / (years * 12)

    if (client_salary * 0.3) > installment:
        print(
            f'Seu emprestimo foi aceito, será pago em {years * 12} parcelas '
            f'de {installment} por mês'
        )
    else:
        print(
            f'Seu emprestimo foi recusado, 30% do seu salário ({client_salary * 0.3}) '
            f'não cobre a parcela de {installment} por mês'
        )


calc_loan()
