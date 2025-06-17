# Projeto: Treinamento de Modelo de Aprendizado de Máquina

Este projeto consiste em um trabalho acadêmico para treinamento e avaliação de modelos de aprendizado de máquina utilizando Python e a biblioteca Pandas. O objetivo é realizar o processamento de dados, treinamento de modelos (como Random Forest), avaliação de desempenho e exposição de resultados via aplicação web.

## Estrutura do Projeto

- **sumario.py**: Logs com o sumário do trabalho.
- **Passo1_CarregaDados.py**: Script responsável por carregar, tratar e exibir informações dos dados de entrada, salvando as saídas dos prints em um arquivo de texto.
- **Passo2_LimpezaBasica.py**: Script responsável por fazer a limpeza dos dados.
- **Passo3_FeatureEngineering.py**: Script responsável por fazer o Label Encoding, padronizar o nome das colunas.
- **Passo4_Visualizacao.py**: Script responsável pela análise exploratória, expondo algumas visualizações das análises efetuadas.
- **Passo5_Treino.py**: Script responsável por treinar o modelo e definir as métricas.
- **start.py**: Arquivo principal para inicialização da aplicação web (Flask), responsável por expor rotas HTTP para visualização dos resultados.
- **Dockerfile**: Define o ambiente de execução do projeto, garantindo reprodutibilidade e facilidade de implantação.
- **.dockerignore**: Lista arquivos e pastas que não devem ser incluídos na imagem Docker.
- **requirements.txt**: Lista de dependências Python do projeto.
- **./data**: Fonte de dados, no formato CSV. A fonte é um DataFrame obtido no [Kaggle](https://www.kaggle.com/datasets/gifreysulay/pavement-dataset)

## Como Executar

### 1. Construir a Imagem Docker

No terminal, execute o comando abaixo na raiz do projeto para construir a imagem Docker:

```sh
docker build -t ml-treinamento .
```

### 2. Executar o Container

Após a construção da imagem, execute o container com:

```sh
docker run -it --rm -p 8000:8000 -v $(pwd):/workspaces/builder ml-treinamento
```

- O parâmetro `-p 8000:8000` expõe a porta 8000 do container para acesso via navegador.
- O parâmetro `-v $(pwd):/workspaces/builder` monta o diretório do projeto no container, permitindo persistência dos arquivos.

### 3. Acessar a Aplicação Web

Após iniciar o container, acesse a aplicação web no navegador:

```sh
$BROWSER http://localhost:8000
```

## Rotas Expostas

A aplicação Flask definida em `start.py` expõe as seguintes rotas:

- **GET /**  
  Exibe a saída do processamento de dados realizado pelos scripts Python, permitindo análise dos dados carregados e tratados.
  Caso treinamento em curso, então será exibido em qual passo que está executando.

- **GET /inicia_treino**  
  Inicia o processo de treinamento, seguindo a seguinte ordem:
    1. Carregamento dos dados
    1. Limpeza dos dados
    1. Feature engineering
    1. Análise exploratório, com exibição dos dados analisados
    1. Execução do treino e medição da acurária

## Observações

- Para treinar o modelo é necessário invocar a rota `/inicia_treino`
- Para visualizar o relatório do treinamento, deve invocar a home, `/`
- Para executar o projeto é necessário ter o Docker instalado.

---