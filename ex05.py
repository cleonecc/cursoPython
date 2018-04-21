# programa que solicita um tamanho em metros e converte para centrímetros

# pede o tamanho em metro e converte para número fracionário (float)
tamanho_em_metro = float(input("Informe o tamanho em metros: "))
tamanho_final = tamanho_em_metro * 100
# para separar a parte decimal da parte fracionária usar o ponto final (.)
print(tamanho_em_metro, " metro(s) corresponde a ", tamanho_final, " centímetros.")