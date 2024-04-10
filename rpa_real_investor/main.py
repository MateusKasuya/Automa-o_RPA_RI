# Configurando meus pacotes
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()

chrome_options.add_experimental_option('detach', True)

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service = servico, options = chrome_options)

navegador.implicitly_wait(0.5)

# Acessando a página WEB

navegador.get('https://www.btgpactual.com/')

navegador.find_element('xpath', '//*[@id="navbar"]/btg-pactual-menu/div/div[1]/div[2]/btg-menu-button/button').click()

navegador.find_element('xpath', '//*[@id="navbar"]/btg-pactual-menu/div/div[3]/a[2]').click()