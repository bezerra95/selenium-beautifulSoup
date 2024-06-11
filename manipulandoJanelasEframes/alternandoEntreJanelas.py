from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webbrowser import ChromeDriverManager

# Configurando o driver do Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Acessando uma página
driver.get('https://www.google.com')

# Abrindo uma nova janela (guia)
driver.execute_script("window.open('https://www.bing.com', '_blank');")

# Alternando para a nova janela
driver.switch_to.window(driver.window_handles[1])

# Fechando a nova janela
driver.close()

# Voltando para a janela original
driver.switch_to.window(driver.window_handles[0])
