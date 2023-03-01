def work_bonus() -> None:  # Calcular o bônus por ano de um funcionario

    year = int(input('years of service: '))
    bonus = int(input('bonus for year: '))
    amount = year * bonus
    
    print(amount)


work_bonus()
