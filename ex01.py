salario = float(input('Qual é o seu salário?: '))
reajuste = (10/100) * salario
reajuste1 = (15/100) * salario
x = salario + reajuste
x1 = salario + reajuste1
if salario <= 1250:
    print('O funcionário ganhava R${:.2f}, seu novo salário será R${:.2f}'.format(salario, x1))

else:
    print('O funcionário ganhava R${:.2f}, seu novo salário será R${:.2f}'.format(salario, x))

