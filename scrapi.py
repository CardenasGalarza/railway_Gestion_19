import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService # Similar thing for firefox also!
from subprocess import CREATE_NO_WINDOW # This flag will only be available in windows
import os

chrome_service = ChromeService('chromedriver')
chrome_service.creationflags = CREATE_NO_WINDOW
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging']);
options.add_argument("--headless")
#options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(service=chrome_service, chrome_options=options)
driver.maximize_window()
params = {'behavior': 'allow', 'downloadPath': os.getcwd()}
driver.execute_cdp_cmd('Page.setDownloadBehavior', params)


username = 'caramburu_TDP'
passwordd = 'WebSys29*T*'


driver.get("https://auth.movistaradvertising.com/login?logout")
time.sleep(3)


email = driver.find_element_by_xpath('//INPUT[@id="username"]')
email.send_keys(username)
time.sleep(2)

psw = driver.find_element_by_xpath('//INPUT[@id="password"]')
psw.send_keys(passwordd)
time.sleep(2)

liddni3 = driver.find_element_by_xpath('//BUTTON[@type="submit"][text()="Ingresar"]')
liddni3.click()
time.sleep(3)


sssss = driver.find_element_by_xpath('//*[@id="dropdown-user-menu"]/div/button[1]')
sssss.click()
time.sleep(6)

liddni3 = driver.find_element_by_xpath('//SPAN[@_ngcontent-c1=""][text()="SMSi"]')
liddni3.click()
time.sleep(6)

celu = '925266696'
mensaje = 'prueba5'

cel = driver.find_element_by_xpath('//INPUT[@id="inputGsmList"]')
cel.send_keys(celu)
time.sleep(6)

men = driver.find_element_by_xpath('//TEXTAREA[@id="txtMessage"]')
men.send_keys(mensaje)
time.sleep(6)


liddni3 = driver.find_element_by_xpath('//BUTTON[@id="buttonProcess"]')
liddni3.click()
time.sleep(5)

liddni3 = driver.find_element_by_xpath('//*[@id="buttonSend"]')
liddni3.click()
time.sleep(5)

driver.quit()

