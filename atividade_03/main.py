"""
# TODO - atividade: Crie um programa que faça as seguintes operações:
- Calculdar área de um círculo
- Calcular tamanho de uma circurferencia
- Sair do programa
# NOTE - para cada loop, o programa deverpa limpar o terminal
"""

#variáveis

import math as m
import os


while True:
    
    raio = float(input("Informe o raio do círculo: "))
    area = m.pi * (raio**2)
    circunferencia = (m.pi*2) * raio

    print(f"A área da circunferência é {area:.2f} e a o tamanho da circunferência é {circunferencia:.2f}")

    prosseguir = input("Deseja inserir outro valor do raio para cálculo? (s/n)").lower().strip()

    match prosseguir:
        case "s":
            os.system("cls")
            continue
        case "n":
            os.system("cls")
            print("Até mais!")
            break
        case _:
            print("Opção inválida.")
            break






