from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webbrowser import ChromeDriverManager


# Configurando o driver do Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Definindo uma espera implícita de 10 segundos
driver.implicitly_wait(10)

# Acessando uma página
driver.get('https://www.google.com')

# Localizando o campo de busca (espera implícita entra em ação)
search_box = driver.find_element_by_name('q')
search_box.send_keys('Selenium Python')
