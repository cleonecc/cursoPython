# programa que pergunta quanto a pessoa ganha por hora e o número de horas trabalhadas por mês, calcula e mostra o
# total do salário no referido mês

# solicita valor da hora de trabalho
salario_por_hora = float(input("Quanto você ganha por hora: "))
# solicita horas trabalhadas no mês
horas_trabalhadas_mes = float(input("Quantas horas trabalhou no mês: "))
# calcula valor do salário mensal
salario_mensal = salario_por_hora * horas_trabalhadas_mes
# apresenta o valor do salário final
print("Seu salário será de R$ ", salario_mensal)