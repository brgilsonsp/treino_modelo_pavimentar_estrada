
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def treinar_modelo(dados_carregado):
    print("""-----------------------------------------------------------------------------------------
>>> Inicio passo 5: Treinamento do modelo <<<
          """)
    
    print('* Copia o DataFrame original para manter o objeto recebido no parâmetro inalterado e mantem a função idempotente.')
    dados = dados_carregado.copy()

    print("")
    print("* Definindo os atributos preditores")
    atributos_preditores = ['pci', 'road_type', 'aadt', 'asphalt_type', 'last_maintenance', 'average_rainfall', 'rutting', 'iri']
    X = dados[atributos_preditores]
    print(X)

    print("")
    print("* Definindo os atributos alvo")
    atributo_alvo = ['needs_maintenance']
    Y = dados[atributo_alvo]
    print(Y)

    print("")
    print("* Separando a massa de treino e teste")
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print("")
    print("* Treinamento do modelo com Random Forest")
    modelo = RandomForestClassifier(n_estimators=10, random_state=42)
    modelo.fit(X_train, y_train)
    
    print("")
    print("* Avaliação do modelo")
    y_pred = modelo.predict(X_test)
    acuracia = accuracy_score(y_test, y_pred)
    print(f"Acurácia: {acuracia}")

    print("""
          
>>> Fim passo 5: Treinamento do modelo <<<
-----------------------------------------------------------------------------------------

          
          """)
    return dados