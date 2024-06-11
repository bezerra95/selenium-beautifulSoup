from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webbrowser import ChromeDriverManager


# Configurando o driver do Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Acessando uma página
driver.get('https://www.example.com')

# Obtendo todos os cookies
cookies = driver.get_cookies()
print(cookies)

# Adicionando um cookie
cookie = {'name': 'myCookie', 'value': '123456'}
driver.add_cookie(cookie)

# Excluindo um cookie
driver.delete_cookie('myCookie')

