import os
from game.config import config

def imgshoted():
    diretorio = config.shot
    
    # Obtém todos os arquivos no diretório
    arquivos = os.listdir(diretorio)

    # Filtra apenas os arquivos de imagem (você pode ajustar isso conforme necessário)
    arquivos_imagem = [arquivo for arquivo in arquivos if arquivo.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Ordena os arquivos pelo tempo de modificação (o mais recente primeiro)
    arquivos_imagem.sort(key=lambda x: os.path.getmtime(os.path.join(diretorio, x)), reverse=True)

    if arquivos_imagem:
        arquivo_recente = arquivos_imagem[0]
        caminho_arquivo_recente = os.path.join(diretorio, arquivo_recente)
        
        # Faça o que for necessário com o arquivo mais recente
        print('Arquivo mais recente:', arquivo_recente)
        print('Caminho do arquivo mais recente:', caminho_arquivo_recente)
        
        # Excluir arquivos anteriores
        for arquivo in arquivos_imagem[1:]:
            caminho_arquivo = os.path.join(diretorio, arquivo)
            os.remove(caminho_arquivo)
            print('Arquivo removido:', arquivo)
        
        return caminho_arquivo_recente
    else:
        print('Nenhum arquivo de imagem encontrado no diretório.')
        return None
