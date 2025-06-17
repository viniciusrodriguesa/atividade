"""

# TODO - atividade: Crie um programa que receba do usuário, o nome, o peso em kg, e a altura em metros, e calcule o valor do IMC (Ídice de Massa Corporal).
O programa deve mostrar o valor do IMC arredondado para 2 casas decimais, e mostrar o diagnóstico do usuário com base nos seguintes valores:

# IMC = peso (kg) / (altura (m) x altura (m)) 

- Caso o IMC seja menor que 18.5 = abaixo do peso.
- Caso o IMC seja maior ou igual a 18.5 e menor que 25 = peso ideal.
- Caso o IMC seja maior ou igual a 24.5 e menor que 30 = acima do peso.
- Caso o IMC seja maior ou igual a 30 e menor que 35 = obeso.
- Caso o IMC seja maior ou igual a 35 e menor que 40 = obesidade nível 2.
- Caso o IMC seja maior ou igual a 40 = obesidade mórbida.
# NOTE - o usuário deverá informar o encerramento do programa, ou seja, ele poderá repetir o cálculo quantas vezes quiser.
"""
while True:
    
    try:
        #variáveis
        nome = input("Informe seu nome: ").title().strip()
        peso = float(input("Informe seu peso em Kg: ").replace(",", "."))
        altura = float(input("Informe sua altura em metros: ").replace(",","."))
        imc = peso / altura**2
    

        if imc <= 18.5:
            print(f"Seu IMC é {imc:.2f}. {nome} está abaixo do peso.")
        elif imc > 18.5 and imc <= 25:
            print(f"Seu IMC é {imc:.2f}. {nome} está no peso ideal.")
        elif imc > 24.5 and imc <= 30:
            print(f"Seu IMC é {imc:.2f}. {nome} está acima do peso.")
        elif imc > 30 and imc <= 35:
            print(f"Seu IMC é {imc:.2f}. {nome} está obeso.")
        elif imc > 35 and imc <= 40:
            print(f"Seu IMC é {imc:.2f}. {nome} está em obesidade nível 2.")
        else:
            print(f"Seu IMC é {imc:.2f}. {nome} está em obesidade mórbida.")

        while True:
            prosseguir = input("Deseja refazer o cáculo? (s/n): ").lower().strip()
            if prosseguir == "s" or prosseguir == "n":
                break
            else:
                print("Opção inválida.")
                continue
        match prosseguir:
            case "s":
                continue
            case "n":
                break
    except Exception as e:
        print(f"Não foi possível executar operação. {e}.")
        continue
