from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webbrowser import ChromeDriverManager
from selenium.webdriver.support.ui import Select


# Configurando o driver do Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Acessando uma página com dropdown
driver.get('https://www.example.com/dropdown')

# Localizando o dropdown
dropdown = Select(driver.find_element_by_id('id_do_dropdown'))

# Selecionando uma opção pelo valor
dropdown.select_by_value('valor')

# Selecionando uma opção pelo texto visível
dropdown.select_by_visible_text('Texto da opção')

# Selecionando uma opção pelo índice
dropdown.select_by_index(2)
