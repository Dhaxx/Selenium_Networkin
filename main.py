from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')

# Configurar o caminho para o driver do Chrome
driver_path = 'D:\Programação\Selenium_Networkin\chromedriver\chromedriver.exe'

# Configurar o objeto Service
service = Service(driver_path)

# Inicializar o driver do Chrome
driver = webdriver.Chrome(service=service, options=chrome_options)


def main():
    # Navegar até o site de login
    driver.get('https://www.linkedin.com/')
    input("Pressione Enter para fechar o navegador...")

    # Fazendo Login 
    elem = driver.find_element(By.NAME, "session_key")
    elem.clear()
    elem.send_keys("kaiopablo44@gmail.com")

    # Fechar o navegador
    driver.quit()

if __name__ == "__main__":
    main()