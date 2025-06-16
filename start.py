from sumario import gerar_sumario
from Passo1_CarregaDados import carregar_dados
from Passo2_LimpezaBasica import limpar_dados
from Passo3_FeatureEngineering import converter_campos
from Passo4_Visualizacao import visualizar_em_graficos
from Passo5_Treino import treinar_modelo

gerar_sumario()
data_carregado = carregar_dados()
dados_limpo = limpar_dados(data_carregado)
dados_convertido = converter_campos(dados_limpo)
dados_visualizado = visualizar_em_graficos(dados_convertido)
dados_treinados = treinar_modelo(dados_visualizado)