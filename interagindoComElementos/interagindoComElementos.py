from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webbrowser import ChromeDriverManager

# Configurando o driver do Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Acessando a página do Google
driver.get('https://www.google.com')

# Localizando e clicando no botão "Estou com sorte"
button = driver.find_element_by_name('btnI')
button.click()


