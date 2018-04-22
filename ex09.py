# programa que solicita uma temperatura em graus Farenheit e converte para graus Celsius

# solicita a temperatura em graus Farenheit
temperatura_farenheit = float(input("Informe a temperatura em graus Farenheit: "))
# Converte a temperatura de Farenheit para Celsius
temperatura_celsius = (5 * (temperatura_farenheit - 32) / 9)
# apresenta o resultado da conversão
print(temperatura_farenheit, " graus Farenheit corresponde a ", temperatura_celsius, " graus Celsius.")