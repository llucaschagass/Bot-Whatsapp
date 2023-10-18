import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuração do ChromeDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Se você quiser rodar em modo headless
chrome_options.add_argument('--no-sandbox')  # Necessário para o ambiente do Colab

# Inicialização do driver do Chrome
navegador = webdriver.Chrome(options=chrome_options)
navegador.get("https://web.whatsapp.com/")

# Espera pelo carregamento do WhatsApp Web
wait = WebDriverWait(navegador, 30)
side_loaded = wait.until(EC.presence_of_element_located((By.ID, "side")))

# Carrega dados do Excel
contatos_df = pd.read_excel("C:\\Users\\Lucas\\OneDrive\\Área de Trabalho\\Atividade Severino\\Bot Whatsapp\\Enviar.xlsx")

# Envio de mensagens para cada contato
for i, row in contatos_df.iterrows():
    pessoa = row["Pessoa"]
    numero = row["Número"]
    mensagem = row["Mensagem"]

    link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"
    navegador.get(link)

    wait.until(EC.presence_of_element_located((By.ID, "side")))
    
    input_box = navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    input_box.send_keys(Keys.ENTER)
    
    time.sleep(10)  # Espera antes de enviar a próxima mensagem

# Fechar o navegador após o envio
navegador.quit()











