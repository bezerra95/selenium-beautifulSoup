from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webbrowser import ChromeDriverManager

# Configurando o driver do Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)



# Acessando a página do Google
driver.get('https://www.google.com')

# Localizando elementos

'''
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_css_selector
'''
search_box = driver.find_element_by_name('q')  # Localiza pela tag 'name'



# Interagindo com o elemento
search_box.send_keys('Selenium Python')

# Submetendo o formulário
search_box.submit()
