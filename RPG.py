#RPG

#if and else - Decisoes
#while e for - Para repeticoes
#listas - Para Guardar Varios Itens

import os

print("Bem vindo ao jogo")

# Nome do arquivo para salvar o inventário
arquivo_inventario = "inventario.txt"

# Função para salvar o inventário no arquivo
def salvar_inventario(inventario):
    with open(arquivo_inventario, "w") as arquivo:
        for item in inventario:
            arquivo.write(item + "\n")

# Função para carregar o inventário do arquivo
def carregar_inventario():
    if os.path.exists(arquivo_inventario):
        with open(arquivo_inventario, "r") as arquivo:
            return [linha.strip() for linha in arquivo.readlines()]
    return []


inventario = carregar_inventario()

while True:
    print("\n1. Ir para a Cabana")
    print("2. Ir para a floresta")
    print("3. Sair do Jogo")
    print("4. Ver o inventário")

    escolha = int(input("Qual a sua escolha?: "))

    if escolha == 1:
        print("\nA cabana tem a Excalibur")
        print("1. Pegar a Espada")
        print("2. Ignorar a Espada")
        print("3. Voltar para a Floresta Negra")    

        espada = int(input("O que você faz?: "))

        if espada == 1:
            if "Excalibur" not in inventario:
                inventario.append("Excalibur")
                salvar_inventario(inventario)  # Salva o inventário ao pegar a espada
                print("O player conseguiu a Excalibur!")
            else:
                print("Você já tem a Excalibur!")
        elif espada == 2:
            print("Você ignorou a espada.")
        elif espada == 3:
            print("Você volta para a Floresta Negra.")
        else:
            print("Número inválido.")

    elif escolha == 2:
        print("Você está na Floresta Negra.")
    elif escolha == 3:
        print("Você saiu do jogo.")
        break
    elif escolha == 4:
        if inventario:
            print("Seu Inventário:")
            for item in inventario:
                print(f"- {item}")
        else:
            print("Seu inventário está vazio.")
    else:
        print("Número inválido.")
