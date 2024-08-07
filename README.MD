# Scraper de Vagas - Catho

Este script coleta informações sobre salários e locais de trabalho para a função de "Atendente de Caixa" do site Catho. Ele realiza scraping em múltiplas páginas e salva os dados coletados em um arquivo Excel.

## Como Funciona

- **Número de Páginas**: Você pode alterar o range de iteraração sobre páginas (Vai de acorodo com as páginas disponíveis).
- **Função `extract_data`**:
  - Faz uma solicitação HTTP para a URL fornecida.
  - Usa BeautifulSoup para analisar o conteúdo HTML e encontrar informações de salário e local de trabalho.
  - Adiciona as informações encontradas a uma lista.
- **Loop de Páginas**: Itera sobre todas as páginas especificadas e coleta os dados de cada uma.
- **Salvamento**: Converte os dados coletados em um DataFrame do pandas e salva como um arquivo Excel, você poderá renomeá los `nome_desejado.xlsx`.

## Uso

Para executar o script:

1. **Certifique-se de ter as dependências instaladas**.
   - Instale as dependências usando o comando:
     ```bash
     pip install -r requirements.txt
     ```

2. **Execute o script Python**:
   - Salve o código em um arquivo chamado `script.py` (ou outro nome de sua escolha).
   - Execute o script com o comando:
     ```bash
     python script.py
     ```
