from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webbrowser import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Configurando o driver do Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Acessando uma página
driver.get('https://www.google.com')

# Espera explícita até que o campo de busca esteja presente
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'q'))
)
search_box.send_keys('Selenium Python')