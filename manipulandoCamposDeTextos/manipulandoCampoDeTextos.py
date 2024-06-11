from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webbrowser import ChromeDriverManager


# Configurando o driver do Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


# Acessando a página do Google
driver.get('https://www.google.com')

# Localizando o campo de busca
search_box = driver.find_element_by_name('q')

# Digitando no campo de busca
search_box.send_keys('Selenium Python')

# Limpando o campo de busca
search_box.clear()
