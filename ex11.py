# programa que solicita dois números inteiros e um número real e faz cálculos conforme o enunciado.

import math

numero01 = int(input("Informe um número inteiro: "))
numero02 = int(input("Informe outro número inteiro: "))
numero03 = float(input("Informe um número real: "))

print("O produto do dobro do primeiro com metade do segundo é ",((numero01*2)*(numero02/2)))
print("A soma do triplo com primeiro com terceiro ", numero01*3 + numero03)
print("O terceiro valor elevedo ao cubo corresponde a ", math.pow(numero03,3))