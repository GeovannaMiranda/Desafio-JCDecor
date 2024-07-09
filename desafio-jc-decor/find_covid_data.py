import requests
import pandas as pd

def find_covid_data():
    # URL da API utilizada
    url = "https://covid19-brazil-api.now.sh/api/report/v1"
    
    try:
        # Fazendo requisição http
        response = requests.get(url)
        data = response.json()
        
        df = pd.DataFrame(data['data'])
        
        # Um print para visualizar as colunas existentes
        print(df.columns)
         
        # Selecionando somente as colunas necessarias  
        columns = ['uf', 'state', 'cases', 'deaths', 'suspects', 'refuses']
        df = df[columns]
        
        # Salvando os dados em um arquivo CSV
        df.to_csv('covid_brazil_data.csv', index=False)
        print("Dados salvos com sucesso no arquivo 'covid_brazil_data.csv'")

    # Tratamento de erros    
    except requests.exceptions.RequestException as e:
        print(f"Erro na solicitação HTTP: {e}")
    except Exception as e:
        print(f"Erro ao processar os dados: {e}")

# Executa a função
find_covid_data()
