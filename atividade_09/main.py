
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
    print("6 - Saia do programa.")
    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        
        case "1":
            try:
                usuario = {}
                usuario.update({
                    'nome': str(input("Insira o nome completo: ")),
                    'data': input("Insira a data de nascimento: "),
                    'email': input("Insira o e-mail: "),
                    'cpf': input("Insira o CPF: "),
                    'telefone': input("Insira o número de telefone: "),
                    'genero': input("Informe o seu gênero: "),
                    'data_cadastro' : date.today(),
                    'hora_cadastro': datetime.now().time().strftime('%H:%M:%S')
                })
                lista.append(usuario)

                print("Usuário inserido com sucesso!")
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
            finally:
                continue
        case "3":
            try:
                indice = int(input('Informe o índice a ser alerado: '))
                campo = input('Informe o nome do campo a ser alterado: ')

                indice -= 1

                lista[indice][campo] = input(f'Infome o novo valor do campo {campo}: ')
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
            except Exception is {e}:
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
                






            
                


