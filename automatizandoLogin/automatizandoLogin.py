from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webbrowser import ChromeDriverManager


# Configurando o driver do Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Acessando a página de login
driver.get('https://www.example.com/login')

# Localizando e preenchendo o campo de usuário
campo_usuario = driver.find_element_by_name('username')
campo_usuario.send_keys('seu_usuario')

# Localizando e preenchendo o campo de senha
campo_senha = driver.find_element_by_name('password')
campo_senha.send_keys('sua_senha')

# Submetendo o formulário de login
campo_senha.submit()
