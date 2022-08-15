from selenium import webdriver
from selenium.webdriver.common.by import By

# Criando instância do navegador
navegador = webdriver.Chrome()

# Maximizando a janela do navegador aberto
navegador.maximize_window()

# Navegando até a página de resultados ao investidores da Maglu
navegador.get("https://ri.magazineluiza.com.br/")

# Abrindo apresentação de resultados através do xpath
navegador.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/a[3]').click()