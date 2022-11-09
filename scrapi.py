import glob
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService # Similar thing for firefox also!
from subprocess import CREATE_NO_WINDOW # This flag will only be available in windows

options = Options()
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-features=NetworkService")
#options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-features=VizDisplayCompositor")
options.add_argument('--disable-blink-features=AutomationControlled')

chrome_service = ChromeService('chromedriver')
chrome_service.creationflags = CREATE_NO_WINDOW
options = webdriver.ChromeOptions()
#options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=chrome_service, chrome_options=options)
driver.maximize_window()

params = {'behavior': 'allow', 'downloadPath': os.getcwd()}
driver.execute_cdp_cmd('Page.setDownloadBehavior', params)




username = 'caramburu_TDP'
passwordd = 'WebSys29*T*'


driver.get("https://auth.movistaradvertising.com/login?logout")
time.sleep(3)


xpath = driver.find_element("xpath", '//INPUT[@id="username"]')
xpath.send_keys(username)
time.sleep(2)

xpath = driver.find_element("xpath", '//INPUT[@id="password"]')
xpath.send_keys(passwordd)
time.sleep(2)

xpath = driver.find_element("xpath", '//BUTTON[@type="submit"][text()="Ingresar"]')
xpath.click()
time.sleep(3)


xpath = driver.find_element("xpath", '//*[@id="dropdown-user-menu"]/div/button[2]')
xpath.click()
time.sleep(7)

xpath = driver.find_element("xpath", '//SPAN[@_ngcontent-c1=""][text()="SMSi"]')
xpath.click()
time.sleep(6)

celu = '925266696'
mensaje = 'prueba77'

xpath = driver.find_element("xpath", '//INPUT[@id="inputGsmList"]')
xpath.send_keys(celu)
time.sleep(6)

xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
xpath.send_keys(mensaje)
time.sleep(6)


xpath = driver.find_element("xpath", '//BUTTON[@id="buttonProcess"]')
xpath.click()
time.sleep(5)

xpath = driver.find_element("xpath", '//*[@id="buttonSend"]')
xpath.click()
time.sleep(5)

driver.quit()



