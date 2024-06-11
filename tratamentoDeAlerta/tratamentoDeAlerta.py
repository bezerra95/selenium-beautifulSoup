from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webbrowser import ChromeDriverManager


# Configurando o driver do Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Acessando uma página que gera um alerta
driver.get('https://www.example.com/alert')

# Aceitando o alerta
alerta = driver.switch_to.alert
alerta.accept()

# Cancelando o alerta
# alerta.dismiss()
