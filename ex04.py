# programa que solicita as 4 notas bimestrais, realiza e apresenta o cálculo da média final

# solicita a nota bimestral e converte-a para inteiro
nota_bimestre01 = int(input("Informe a nota do 1º bimestre: "))
# solicita a nota bimestral e converte-a para inteiro
nota_bimestre02 = int(input("Informe a nota do 2º bimestre: "))
# solicita a nota bimestral e converte-a para inteiro
nota_bimestre03 = int(input("Informe a nota do 3º bimestre: "))
# solicita a nota bimestral e converte-a para inteiro
nota_bimestre04 = int(input("Informe a nota do 4º bimestre: "))
# realiza o cálculo da nota final conforme as regras do IFRN
nota_final = ((nota_bimestre01*2)+(nota_bimestre02*2)+(nota_bimestre03*3)+(nota_bimestre04*3))/10
# apresenta a nota final
print("Sua média final é ", nota_final)