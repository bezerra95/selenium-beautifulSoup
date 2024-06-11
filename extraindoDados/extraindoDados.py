from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webbrowser import ChromeDriverManager


# Configurando o driver do Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


# Acessando uma página
driver.get('https://www.example.com')

# Extraindo texto de um elemento
elemento = driver.find_element_by_id('id_do_elemento')
texto = elemento.text
print(texto)

# Extraindo um atributo de um elemento
atributo = elemento.get_attribute('atributo')
print(atributo)
