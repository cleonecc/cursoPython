# programa que solicita uma temperatura em graus Celsius e converte para graus Farenheit

# solicita a temperatura em graus Celsius
temperatura_celsius = float(input("Informe a temperatura em graus Celsius: "))
# Converte a temperatura de Celsius para Farenheit
temperatura_farenheit = temperatura_celsius * 1.8 + 32
# apresenta o resultado da conversão
print(temperatura_celsius, " ºC corresponde a ", temperatura_farenheit, " ºF. ")
