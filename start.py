from sumario import gerar_sumario
from Passo1_CarregaDados import carregar_dados
from Passo2_LimpezaBasica import limpar_dados
from Passo3_FeatureEngineering import converter_campos
from Passo4_Visualizacao import visualizar_em_graficos
from Passo5_Treino import treinar_modelo
from flask import Flask, render_template_string
import sys
import threading
import os

diretorio_conteudo_resultado="./static/resultado"
encoding='utf-8'
etapa_atual="Desconhecida"

app = Flask(__name__)

@app.route("/inicia_treino")
def inicia_treino():
    global etapa_atual
    if nao_esta_em_treinamento():
        threading.Thread(target=processar_treino, daemon=True).start()
        
    return retornar_resultado_iniciado()

    
def processar_treino():
    criar_diretorio_resultado_vazio()
    caminho_conteudo_resultado = diretorio_conteudo_resultado + "/resultado.txt"
    sys.stdout = open(caminho_conteudo_resultado, 'w', encoding=encoding)
    gerar_sumario()
    global etapa_atual
    etapa_atual = "Passo 1 - Carregando dados"
    data_carregado = carregar_dados()
    etapa_atual = "Passo 2 - Limpando dados"
    dados_limpo = limpar_dados(data_carregado)
    etapa_atual = "Passo 3 - Convertendo campos"
    dados_convertido = converter_campos(dados_limpo)
    etapa_atual = "Passo 4 - Visualizando dados"
    dados_visualizado = visualizar_em_graficos(dados_convertido)
    etapa_atual = "Passo 5 - Treinando modelo"
    treinar_modelo(dados_visualizado)
    etapa_atual = "Treinamento concluído"
    sys.stdout.close()

def criar_diretorio_resultado_vazio():

    if not os.path.exists(diretorio_conteudo_resultado):
        os.makedirs(diretorio_conteudo_resultado)
    else:
        excluir_arquivos_existentes(diretorio_conteudo_resultado)

    return diretorio_conteudo_resultado

def excluir_arquivos_existentes(diretorio_saida):
    for nome in os.listdir(diretorio_saida):
        caminho = os.path.join(diretorio_saida, nome)
        if os.path.isfile(caminho):
            os.remove(caminho)

def retornar_resultado_iniciado():
    return """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Treinamento Modelo</title>
        <style>
            body { font-family: monospace; background: #f9f9f9; padding: 2em; }
            pre { background: #eee; padding: 1em; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>Inicio treinamento</h1>
        <p>O treinamento foi iniciado com sucesso!</p>
        <p>Você pode acessar o resultado <a href="/" target="_blank">clicando aqui</a>.</p>
    </body>
    </html>
    """

@app.route("/")
def exibe_prints():

    if nao_esta_em_treinamento():
        return retornar_resultado_concluido()
    else:
        return retornar_resultado_em_andamento()

def retornar_resultado_concluido():
    caminho_conteudo_resultado = diretorio_conteudo_resultado + "/resultado.txt"
    try:
        with open(caminho_conteudo_resultado, encoding=encoding) as f:
            conteudo = f.read()
            html = retornar_html_resultado_concluido()
            return render_template_string(html, conteudo=conteudo)
    except FileNotFoundError:
        return retornar_html_resultado_nao_iniciado()

    
def retornar_html_resultado_concluido():
    return """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Treinamento Modelo</title>
        <style>
            body { font-family: monospace; background: #f9f9f9; padding: 2em; }
            pre { background: #eee; padding: 1em; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>Resultado do treinamento</h1>
        <pre>{{ conteudo }}</pre>
        <h2>Visualizações</h2>
        <img src="./static/images/01_distribuicoes_principais.png" alt="Visualização inicial das distribuições das variáveis principais" style="max-width: 100%; height: auto;">
        <br>
        <br>
        <img src="./static/images/02_analise_categorica.png" alt="Visualização análise categórica" style="max-width: 100%; height: auto;">
    </body>
    </html>
    """

def retornar_html_resultado_nao_iniciado():
    return """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Treinamento Modelo</title>
        <style>
            body { font-family: monospace; background: #f9f9f9; padding: 2em; }
            pre { background: #eee; padding: 1em; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>Resultado do treinamento</h1>
        <p>Não foi encontrado resultado de treinamento. Você pode iniciar o treinamento <a href="/inicia_treino" target="_blank">clicando aqui</a>.</p>
    </body>
    </html>
    """


def retornar_resultado_em_andamento():
    return f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Treinamento Modelo</title>
        <style>
            body {{ font-family: monospace; background: #f9f9f9; padding: 2em; }}
            pre {{ background: #eee; padding: 1em; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <h1>Status treino</h1>
        <p>O treinamento ainda está em andamento, por favor, aguarde e tente novamente!</p>
        <p>Etapa atual: { etapa_atual }</p>
    </body>
    </html>
    """

def nao_esta_em_treinamento():
    global etapa_atual
    return etapa_atual == "Desconhecida" or etapa_atual == "Treinamento concluído"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
