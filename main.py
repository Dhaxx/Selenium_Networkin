from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

buscando = True

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
import time

driver = webdriver.Chrome(r".\chromedriver\chromedriver.exe", options=chrome_options)

def main():
    # Navegar até o site de login
    driver.get('https://www.linkedin.com/')

    # Fazendo Login 
    email = driver.find_element(By.XPATH, "//input[@name = 'session_key']")
    password = driver.find_element(By.XPATH, "//input[@name = 'session_password']")

    with open(r"D:\\Programação\\Selenium_Networkin\\USER.txt") as myUser:
        username = myUser.read().replace('\n', '')
    email.send_keys(username)

    with open(r"D:\\Programação\\Selenium_Networkin\\PASSWORD.txt") as myPass:
        passcode = myPass.read().replace('\n', '')
    password.send_keys(passcode)

    submit = driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
    time.sleep(3)

    # Buscando por palavra chave
    driver.get('https://www.linkedin.com/search/results/all/?keywords=programa%C3%A7%C3%A3o&origin=GLOBAL_SEARCH_HEADER&sid=oW%40')
    time.sleep(2)

    pessoas = driver.find_element(By.XPATH, "//button[text() ='Pessoas']").click()
    time.sleep(3)

    while buscando:
        pessoas = driver.find_elements(By.XPATH, "//button[span[text()='Conectar']]")

        for pessoa in pessoas:
            pessoa.click() 
            botao_adicionarNota = driver.find_element(By.XPATH, "//button[span[text()='Adicionar nota']]").click()
            nome = (driver.find_element(By.XPATH, "//h2[@id = 'send-invite-modal']").text).split()
            mensagem = (f"""Olá {nome[1]}! Estou entrando em contato porque tenho um grande interesse em programação e estou sempre em busca de encontrar novas formas de criar comunicações impactantes. Gostaria de explorar possíveis colaborações e descobrir oportunidades empolgantes nesse campo. Seria ótimo conectar com você!""")
            text_area = (driver.find_element(By.XPATH,"//textarea[@name = 'message']"))
            text_area.send_keys(mensagem)
            btn_enviarNota = driver.find_element(By.XPATH,"//button[span[text() = 'Enviar']]").click()
            time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(5)
        btn_avancar = driver.find_element(By.XPATH,"//button[span[text() = 'Avançar']]").click()
        time.sleep(3)
        continue


if __name__ == "__main__":
    main()