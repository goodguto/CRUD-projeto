





















































import os
os.system('cls')

arquivo_treino = "aquivo.txt"
def carregar_treinos():
    if os.path.exists(arquivo_treino):
        with open(arquivo_treino, "r") as file:
            return [linha.strip() for linha in file.readlines()]
    return []


def salvar_treinos(treinos):
    with open(arquivo_treino, "w") as file:
        for treino in treinos:
            file.write(f"{treino}\n")

novo_treino = carregar_treinos()


novo_treino = []
while True:
    print("MENU:")
    print("1-> Criar treinos. ")
    print("2-> Visualizar treinos. ")
    print("3-> Atualizar treinos. ")
    print("4-> Deletar treinos. ")
    print("5-> Sair. ")

    opcao = str(input("Escolha uma opção: "))

    if opcao == '1':
        treino = str(input("Digite o treino que você deseja criar "))
        novo_treino.append(treino)
        salvar_treinos(novo_treino)
        print(f"O novo treino é: {novo_treino}.")

    elif opcao == '2':
        if len(novo_treino) == 0:
            print("Não existe treinos ainda.")
        else:
            print("\nLista de treinos: ")
            for i,treino in enumerate(novo_treino):
                print(f"Os treinos cadastrados são: \n{i+1}º treino:{novo_treino}")
    elif opcao == '3':
        if len(novo_treino) == 0:
            print("Não há treinos para atualizar.")
        else:
            print("\nLista de treinos: ")
            for i,treino in enumerate(novo_treino):
                print(f"\n{i+1}º treino:{novo_treino}")
                atualizar = int(input("Escolha o treino que deseja atualizar: "))

                if atualizar > 0 and atualizar <len(novo_treino):
                    novo_treino[atualizar] = str(input("Digite o novo treino para sua lista."))
                    salvar_treinos(novo_treino)
                    print("Treino redefinido.")
                else:
                    print("Treino não encontrado")
    elif opcao == '4':
        if len(novo_treino) == 0:
            print("Não há treinos para atualizar.")
        else:
            print("\nLista de treinos: ")
            for i,treino in enumerate(novo_treino):
                print(f"\n{i+1}º treino:{novo_treino}")
            
            deletar = int(input("Digite o treino que deseja deletar."))
            if deletar> 0 and deletar<len(novo_treino):
                remover = novo_treino.pop(deletar)
                salvar_treinos(novo_treino)
                print(f"O treino '{remover}, foi deletado.'")
            else:
                print("Não há treinos para deletar.")
    else:
        print("Opção não encontrada. ")