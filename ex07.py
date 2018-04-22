# programa que calcula a área de um quadrado e mostra o dobro da área calculada

# solicita o valor referente ao lado do quadrado
lado_quadrado = int(input("Informe o tamanho do lado do quadrado: "))
# calcula a área do quadrado
area_quadrado = lado_quadrado ** 2
# multiplica o valor da área do quadrado por 2
tamanho_final = area_quadrado * 2
# apresenta o resultado final
print("O dobro da área calculada é ", tamanho_final)
