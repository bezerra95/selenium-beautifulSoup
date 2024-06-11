from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webbrowser import ChromeDriverManager


# Configurando o driver do Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Acessando uma página
driver.get('https://www.example.com')

# Fazendo captura de tela da página inteira
driver.save_screenshot('screenshot.png')

# Fazendo captura de tela de um elemento específico
elemento = driver.find_element_by_id('id_do_elemento')
elemento.screenshot('elemento.png')
