import pandas as pd

def carregar_dados():
    print("""-----------------------------------------------------------------------------------------
>>> Inicio passo 1: Carregamento dos dados <<<
          """)
    path_file = './data/required_pavement.csv'
    dados = pd.read_csv(path_file, encoding='utf-8', sep=',')
    print(f"""
* Arquivo {path_file} carregado com sucesso!
          
          
* Informações do DataFrame:
          """)
    print(dados.info())
    print("""
          
          
* Descrição do DataFrame:
          """)
    print(dados.describe())
    print("""
          
          
 * Valores do DataFrame:
          """)
    print(dados)

    print("""
          

>>> Fim passo 1: Carregamento dos dados <<<
-----------------------------------------------------------------------------------------

          """)
    return dados