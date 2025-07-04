"""
# TODO - Atividade: faça um CRUD (Create, Read, Update, Delete) em um JSON.

Opções do menu:

- Criar novo arquivo JSON. (Usuário irá informar o diretorio)
- Abrir arquivo JSON (Usuário irá informar o diretorio)
- Cadastar novo usuário em um JSON.
- Listar todos os usuários de um arquivo JSON.
- Pesquisar por um usuário de um arquivo JSON.
- Alterar dados de um usuário em um arquivo JSON.
- Deletar usuário de um arquivo JSON.
- Sair do Programa.

Dados do usuário:
- Nome
- Data de nascimento
- CPF
- Email
- Telefone
- Filme favorito
"""
import json
import os

usuarios = []

while True:
    usuario = {}
    print("1 - Cadastrar novo arquivo JSON.")
    print("2 - Abrir arquivo JSON.")
    print("3 - Cadastrar novo usuário.")
    print("4 - Listar todos os usuários.")
    print("5 - Pesquisar usuário por chave.")
    print("6 - Alterar dados de um usuário.")
    print("7 - Alterar dados de um usuário.")
    print("8 - Deletar usuário.")
    print("9 - Sair do programa.")
    opcao = input("Informe opção desejada:")
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            novo_arquivo = input("informe o nome do arquivo").strip().title()
            dir = input("informe nome do diretório: ").strip()
            with open(f"{dir}/{novo_arquivo}.json", "w", encoding="utf-8") as f:
                json.dump([], f)
        case "2":
            novo_arquivo = input("Informe o nome do arquivo para ser aberto: ").strip().lower()
            dir = input("informe nome do diretório em que o arquivo se encontra: ").strip()
            with open(f"{dir}/{novo_arquivo}.json", "r", encoding="utf-8") as f:
                dados = json.load(f)
            print(dados)
        case "3":
            usuario['nome'] = input("Informe o nome: ").strip().lower()
            usuario['dt_nascimento'] = input("Informe o data de nascimento: ").strip().lower()
            usuario['cpf'] = input("Informe o CPF: ").strip()
            usuario['telefone'] = input("Informe o Telefone: ").strip()
            usuario['f_fav'] = input("Informe o filme favorito: ").strip()

            arquivo = input("informe o nome do arquivo que dejesa salvar os dados: ").strip().lower()
            dir = input("informe nome do diretório em que o arquivo se encontra: ").strip()
        

            with open(f"{dir}/{arquivo}.json", "r", encoding="utf-8") as f:
                dados = json.load(f)

            usuarios.append(usuarios)

            with open(f"{dir}/{arquivo}.json", "w", encoding="utf-8") as f:
                json.dump(usuarios, f)

            
     

            os.system("cls" if os.name == "nt" else "clear")

            print("Usuário cadastrado com sucesso.")

        case "4":
            ...
        case "5":
            ...
        case "6":
            ...
        case "7":
            ...
        case "8":
            ...
        case "9":
            print("Programa finalizado.")
            break
        case "_":
            print("Opção inválida.")
            continue