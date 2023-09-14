import os
import shutil
import random

diretorio_raiz = "/home/lucasleite/Todas as Classes/Insetos" # Diretório raiz onde estão as pastas originais

# Pastas originais
# Retorna de forma automática as pastas originais de diretorio raiz
pastas_originais = [nome for nome in os.listdir(diretorio_raiz) if os.path.isdir(os.path.join(diretorio_raiz, nome))]

# Porcentagem de imagens para treinamento
porcentagem_treino = 0.8

for pasta in pastas_originais:
    pasta_origem = os.path.join(diretorio_raiz, pasta)
    pasta_destino_treino = os.path.join(diretorio_raiz, "Treino", pasta)
    pasta_destino_teste = os.path.join(diretorio_raiz, "Teste", pasta)

    # Criamos as pastas de treinamento e teste
    os.makedirs(pasta_destino_treino, exist_ok=True)
    os.makedirs(pasta_destino_teste, exist_ok=True)

    arquivos = os.listdir(pasta_origem)

    random.shuffle(arquivos) # Embaralhamos a lista de arquivos (opcional)

    # Calculamos o número de imagens para treinamento
    num_treino = int(len(arquivos) * porcentagem_treino)

    # Separamos as imagens para treinamento e teste
    imagens_treino = arquivos[:num_treino]
    imagens_teste = arquivos[num_treino:]

    # Copiamos as imagens para as pastas de treinamento e teste
    for arquivo in imagens_treino:
        origem_arquivo = os.path.join(pasta_origem, arquivo)
        destino_arquivo = os.path.join(pasta_destino_treino, arquivo)
        shutil.copy(origem_arquivo, destino_arquivo)

    for arquivo in imagens_teste:
        origem_arquivo = os.path.join(pasta_origem, arquivo)
        destino_arquivo = os.path.join(pasta_destino_teste, arquivo)
        shutil.copy(origem_arquivo, destino_arquivo)

print("Divisão concluída.")
