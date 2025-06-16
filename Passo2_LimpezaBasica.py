
def limpar_dados(dados_carregado):
    print("""-----------------------------------------------------------------------------------------
>>> Inicio passo 2: Limpeza dos dados <<<
          """)
    print('* Copia o DataFrame original para manter o objeto recebido no parâmetro inalterado e mantem a função idempotente.')
    dados = dados_carregado.copy()
    
    print("""

* Remove coluna Segment ID, pois não é necessária para a análise.""")
    dados.drop(columns=['Segment ID'], inplace=True)

    print("""
          
* Informação do DataFrame após limpeza:""")
    print(dados.info())

    print("""
          
* Valores do DataFrame após limpeza:""")
    print(dados.head())

    print("""
          

>>> Fim passo 2: Limpeza dos dados <<<
-----------------------------------------------------------------------------------------

          """)
    return dados