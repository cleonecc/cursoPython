# programa que solicita o raio de um círculo, calcula e mostra a área desta figura geométrica

# importa a biblioteca matemática
import math

raio = float(input("Informe o raio do círculo: "))
area = math.pi * math.pow(raio,2)
print("A área do círculo é ", area)