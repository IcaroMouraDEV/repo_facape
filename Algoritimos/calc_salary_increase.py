def calc_salary_increase():
    salary = float(input('Informe o seu salario: '))

    if salary > 1250:
        print(f'seu novo salario é {salary * 0.1 + salary}R$')
    else:
        print(f'seu novo salario é {salary * 0.15 + salary}R$')


calc_salary_increase()
