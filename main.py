#

from pathlib import Path

def salvar_lista(nome_arquivo, lista):
    caminho_do_arquivo = Path(nome_arquivo)
    with caminho_do_arquivo.open(mode='w') as arquivo:
        for item in lista:
            arquivo.write(f"{item}\n")
    print(f"Dados salvos em '{nome_arquivo}' com sucesso!")

def carregar_lista(nome_arquivo):
    caminho_do_arquivo = Path(nome_arquivo)
    if not caminho_do_arquivo.exists():
        print(f"O arquivo '{nome_arquivo}' não foi encontrado. Começando com inventário vazio.")
        return []
    with caminho_do_arquivo.open(mode='r') as arquivo:
        dados_lidos = arquivo.readlines()
    return [item.strip() for item in dados_lidos]
