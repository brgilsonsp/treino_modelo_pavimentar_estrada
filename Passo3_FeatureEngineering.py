
def converter_campos(dados_carregado):
    print("""-----------------------------------------------------------------------------------------
>>> Inicio passo 3: Feature Engineering, converter campos <<<
          """)
    print('* Copia o DataFrame original para manter o objeto recebido no parâmetro inalterado e mantem a função idempotente.')
    dados = dados_carregado.copy()

    print("")
    print(f"* Renomear nomes das colunas padrão snake_case")
    dados = dados.rename(columns= {
        'PCI': 'pci',
        'Road Type': 'road_type',
        'AADT': 'aadt',
        'Asphalt Type': 'asphalt_type',
        'Last Maintenance': 'last_maintenance',
        'Average Rainfall': 'average_rainfall',
        'Rutting': 'rutting',
        'IRI': 'iri',
        'Needs Maintenance': 'needs_maintenance'
    })

    print(f"""
* Label Encoding da coluna "{dados.road_type.name}" para converter categorias em números.
   Utilizado o método 'cat.codes' do pandas para converter categorias em códigos numéricos.""")
    dados.road_type = dados.road_type.astype('category').cat.codes


    print(f"""
* Label Encoding da coluna "{dados.asphalt_type.name}" para converter categorias em números.
   Utilizado o método 'cat.codes' do pandas para converter categorias em códigos numéricos.""")
    dados.asphalt_type = dados.asphalt_type.astype('category').cat.codes

    print("")
    print("* Informação do DataFrame após feature engineering:")
    print(dados.info())

    print("")
    print("* Valores do DataFrame após feature engineering:")
    print(dados.head(10))

    print("""
          
>>> Fim passo 3: Feature Engineering, converter campos <<<
-----------------------------------------------------------------------------------------

          
          """)
    return dados