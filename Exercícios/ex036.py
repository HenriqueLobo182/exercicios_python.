# Escreva um programa para aprovar o empréstimo bancário de uma casa. O programa vai perguntar o valor da casa, o
# salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

colors = {'red': '\033[31m', 'green': '\033[32m', 'clean': '\033[m'}

houseValue = float(input('House value: R$')) 
employeeSalary = float(input('Employee salary: R$')) 
years_of_payment = int(input('Years of payment: '))  

monthlyInstallment = houseValue / (years_of_payment*12)
loanApproval = monthlyInstallment <= (employeeSalary*0.30)

if loanApproval:
    print(f"{colors['green']}Loan accepted!{colors['clean']} The monthly loan amount will be R${monthlyInstallment:.2f}")
else:
    print(f"{colors['red']}Loan dennied!{colors['clean']} The monthly amount of R${monthlyInstallment:.2f} of the loan exceeds 30% of the employee's salary")
