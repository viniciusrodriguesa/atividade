
from datetime import date
from datetime import datetime
import random
import os

lista = []

while True:

    
    print("1 - Cadastre um novo usuário.")
    print("2 - Liste todos os usuários cadastrados.")
    print("3 - Altere os dados de um usuário.")
    print("4 - Faça um sorteio dos usuários.")
    print("5 - Exclua um usuário.")
    print("6 - Sair do programa.")
    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        
        case "1":
            try:
                usuario = {}
                usuario.update({
                    'nome': str(input("Insira o nome completo: ").strip().title()),
                    'data': input("Insira a data de nascimento: ").strip(),
                    'email': input("Insira o e-mail: ").strip().lower(),
                    'cpf': input("Insira o CPF: ").strip(),
                    'telefone': input("Insira o número de telefone: ").strip(),
                    'genero': input("Informe o seu gênero: ").strip(),
                    'data_cadastro' : date.today().strftime("%d/%m/%Y"),
                    'hora_cadastro': datetime.now().time().strftime('%H:%M:%S')
                })
                lista.append(usuario)

                os.system("cls" if os.name == "nt" else "clear")

                print(f"Usuário {usuario.get('nome')} inserido com sucesso!")
            except Exception as e:
                print(f"Não foi possível inserir novo usuário. {e}.")
            finally:
                 continue
        case "2":
            try:
                if not lista:
                    print("Nenhum usuário cadastrado.")
                else:
                    for i in range(len(lista)):
                        print(f'Índice:{ i + 1}')                    
                        print(f'Nome:{lista[i]['nome']}')
                        print(f'Data:{lista[i]['data']}')
                        print(f'E-mail:{lista[i]['email']}')
                        print(f'CPF:{lista[i]['cpf']}')
                        print(f'Telefone:{lista[i]['telefone']}')                  
                        print(f'Gênero:{lista[i]['genero']}')
                        print(f'Data do cadastro:{lista[i]['data_cadastro']}')
                        print(f'Hora do cadastro:{lista[i]['hora_cadastro']}')
                        print("-"*40)
            finally:
                continue
        case "3":
            try:
                indice = int(input('Informe o índice a ser alerado: '))
                os.system("cls" if os.name == "nt" else "clear")
                if i >= 0 and i < len(lista):
                    print(f"{"-"*20} Dados do usuário {'-'*20}")
                    for chave in lista[i]:
                        print(f"{chave.captalize()}: {lista[i].get(chave)}") #destrinchar esse código para melhor entedimento
                    print('\n')
                    while True:

                        campo = input('Informe o nome do campo a ser alterado: ').strip().lower()


                        if campo in lista[i]:

                            lista[indice][campo] = input(f'Infome o novo valor do campo {campo}: ')
                            os.system("cls" if os.name == "nt" else "clear")
                            print("Chave alterar com sucesso.")

                else:
                    print("Índice inválido")
                while True:
                    prosseguir = input("Deseja alterar outra chave? (s/n): ").strip().lower()
                    if prosseguir == "s" or prosseguir == "n":
                        break
                    else:
                        continue
                match prosseguir:
                    case "s":
                        continue
                    case "n":
                        break
            except:
                print('Não foi possível alterar.')
            finally:
                continue
        case "4":
            try:
                indice_sorteado = random.randint(0, len(lista)-1)
                print(f'Índice:{indice_sorteado}')                    
                print(f'Nome:{lista[indice_sorteado]['nome']}')
                print(f'Data:{lista[indice_sorteado]['data']}')
                print(f'E-mail:{lista[indice_sorteado]['email']}')
                print(f'CPF:{lista[indice_sorteado]['cpf']}')
                print(f'Telefone:{lista[indice_sorteado]['telefone']}')                  
                print(f'Gênero:{lista[indice_sorteado]['genero']}')
                print(f'Data do cadastro:{lista[indice_sorteado]['data_cadastro']}')
                print(f'Hora do cadastro:{lista[indice_sorteado]['hora_cadastro']}')
            except Exception is e:
                print(f"Não foi possível realizar o sorteio {e}")
            finally:
                continue
        case "5":
            try:
                indice = int(input('Informe o índice que deseja deletar da lista de dicionários: '))
                indice -= 1
                del[lista[indice]]
            except Exception is e:
                print(f"Não foi possível deletar o usuário. {e}")
            finally:
                continue
        case "6":
            print("Programa finalizado!")
            break
       
        case _:
            print("Opção inválida.")
            continue
                






            
                


