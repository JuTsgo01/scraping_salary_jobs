#%%
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Número de páginas máximas que tem 
pages = range(1, 66)

#Função para pegar salário e local (cidade/UF)
def extract_data(url: str) -> list[str]:
    data_list = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        all_contents = soup.find_all('li', class_='search-result-custom_jobItem__OGz3a')
        
        for all_content in all_contents:
            salary_div = all_content.find('div', class_='custom-styled_salaryText__oSvPo')
            local_link = all_content.find('a', title=True)
            
            salary = salary_div.get_text(strip=True) if salary_div else 'Não informado'
            local = local_link.get('title') if local_link else 'Não informado'
            
            data_list.append([salary, local])

    else:
        print(f"Erro ao acessar a página {url}: {response.status_code}")
    return data_list

#Lista para armazenar todos os dados que a função retorna
data_jobs = []

#Loop para iterar sobre as páginas e pegarmos as funções em cada página
for page in pages:
    url = f"https://www.catho.com.br/vagas/operador-de-caixa/?page={page}&work_model%5B0%5D=presential"
    jobs = extract_data(url)
    data_jobs.extend(jobs)


#Tranformando um dataframe e salvando como excel
df = pd.DataFrame(data_jobs, columns=['salario', 'cidade'])
df.to_excel('catho_caixa_atendente.xlsx', index=False)