# programa que solicita ao usuário sua altura, calcula o peso ideal segundo a fórmula (72.7 * altura) - 58

# solicita a altura do indivíduo e converte-a para número fracionário
altura = float(input("Informe sua altura: "))
# calcula o peso ideal
peso_ideal = (72.7 * altura) - 58
# apresenta o peso ideal da pessoa
print("Seu peso ideal é ", peso_ideal)