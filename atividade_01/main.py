# Laço de repetição
while True:
    # tratamento de exceção
    try:
        # entrada de dados
        etanol = float(input("Informe valor do etanol: ").replace(",", "."))
        gasolina = float(input("Informe valor do etanol: ").replace(",", "."))
        calculo = (etanol/gasolina)*100
        result = "gasolina" if etanol > gasolina*0.7 else "etanol"

        print(f"Resultado = {calculo:.2f}%. Compensa abastecer com {result}. ")


        opcao = input("Deseja refazer o cáculo? (s/n)").lower().strip()
        match opcao:
            case "s":
                continue
            case "n":
                break
            case _:
                print("Opção inválida.")
                continue
    except Exception as e:
        print(f"Não foi possível executar operação. {e}.")
        continue

#informar melhor valor
# usuario pode informar varias vezes o valor 
# compensa etanol caso ele tenha ate 70 por cento da gasolina 