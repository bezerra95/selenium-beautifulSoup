from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webbrowser import ChromeDriverManager


# Configurando o driver do Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


# Acessando uma página com frames
driver.get('URL_DA_PAGINA_COM_FRAMES')

# Alternando para um frame
driver.switch_to.frame('nome_do_frame')

# Realizando ações dentro do frame
elemento_dentro_do_frame = driver.find_element_by_id('id_do_elemento')
elemento_dentro_do_frame.click()

# Voltando para o contexto principal
driver.switch_to.default_content()
