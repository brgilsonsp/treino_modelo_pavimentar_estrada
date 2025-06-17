import seaborn as sns
import matplotlib.pyplot as plt
import os
import warnings

warnings.filterwarnings('ignore')

def visualizar_em_graficos(data_carregado):
    print("""-----------------------------------------------------------------------------------------
>>> Inicio passo 4: Visualização dos dados <<<
          """)
    
    print('* Copia o DataFrame original para manter o objeto recebido no parâmetro inalterado e mantem a função idempotente.')
    dados = data_carregado.copy()
    diretorio_saida = criar_diretorio_visualizacoes_vazio()
    visualizar_exploracao_inicial(dados, diretorio_saida)
    visualizar_analise_categorica(dados, diretorio_saida)

    print("""
          
>>> Fim passo 4: Visualização dos dados <<<
-----------------------------------------------------------------------------------------

          
          """)
    return dados

def visualizar_exploracao_inicial(dados, diretorio_saida):

    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Distribuições das Variáveis Principais por quantidade de estradas', fontsize=16, fontweight='bold')

    sns.histplot(data=dados, x='pci', kde=True, ax=axes[0,0])
    axes[0,0].set_title('Distribuição do PCI (Pavement Condition Index)')
    axes[0,0].set_xlabel('PCI')

    sns.histplot(data=dados, x='aadt', kde=True, log_scale=True, ax=axes[0,1])
    axes[0,1].set_title('Distribuição do AADT (Tráfego Médio Diário)')
    axes[0,1].set_xlabel('AADT (escala log)')

    sns.histplot(data=dados, x='average_rainfall', kde=True, ax=axes[1,0])
    axes[1,0].set_title('Distribuição da Precipitação Média')
    axes[1,0].set_xlabel('Precipitação Média (mm)')

    sns.histplot(data=dados, x='last_maintenance', kde=True, ax=axes[1,1])
    axes[1,1].set_title('Distribuição do período da última manutenção')
    axes[1,1].set_xlabel('Última Manutenção')

    plt.tight_layout()
    plt.savefig(f'{diretorio_saida}/01_distribuicoes_principais.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("")
    print("* Distribuições das variáveis principais. Imagem será exibida na sessão Visualizações, no final da página.")
    

def visualizar_analise_categorica(dados, diretorio_saida):
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Análise por Categorias', fontsize=16, fontweight='bold')

    sns.boxplot(data=dados, x='road_type', y='pci', ax=axes[0,0])
    axes[0,0].set_title('PCI por Tipo de Estrada')
    axes[0,0].set_xlabel('Tipo de Estrada (Primária, Secundária, etc.)')

    sns.boxplot(data=dados, x='asphalt_type', y='pci', ax=axes[0,1])
    axes[0,1].set_title('PCI por Tipo de Asfalto')
    axes[0,1].set_xlabel('Tipo de Asfalto (Concreto ou Asfalto)')

    df_maint = dados.groupby(['road_type', 'needs_maintenance']).size().unstack()
    df_maint_pct = df_maint.div(df_maint.sum(axis=1), axis=0) * 100
    sns.heatmap(df_maint_pct, annot=True, fmt='.1f', cmap='RdYlBu_r', ax=axes[1,0])
    axes[1,0].set_title('% Necessidade de Manutenção por Tipo de Estrada')
    axes[1,0].set_xlabel('Necessita de Manutenção')
    axes[1,0].set_ylabel('Tipo de Estrada (Primária, Secundária, etc.)')

    sns.histplot(data=dados, x='last_maintenance', y='pci', ax=axes[1,1])
    axes[1,1].set_title('Distribuição: Anos desde Última Manutenção por PCI')
    axes[1,1].set_xlabel('Período da manutenção (anos)')
    axes[1,1].set_ylabel('PCI')

    plt.tight_layout()
    plt.savefig(f'{diretorio_saida}/02_analise_categorica.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("")
    print("* Análise categórica. Imagem será exibida na sessão Visualizações, no final da página.")
    

def criar_diretorio_visualizacoes_vazio():
    diretorio_saida = './static/images'

    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)
    else:
        excluir_arquivos_existentes(diretorio_saida)

    return diretorio_saida

def excluir_arquivos_existentes(diretorio_saida):
    for nome in os.listdir(diretorio_saida):
        caminho = os.path.join(diretorio_saida, nome)
        if os.path.isfile(caminho):
            os.remove(caminho)