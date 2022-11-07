import time
from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

params = {'behavior': 'allow', 'downloadPath': os.getcwd()}
driver.execute_cdp_cmd('Page.setDownloadBehavior', params)



username = 'caramburu_TDP'
passwordd = 'WebSys29*T*'


driver.get("https://auth.movistaradvertising.com/login?logout")
time.sleep(3)

xpath = driver.find_element_by_xpath('//INPUT[@id="username"]')
xpath.send_keys(username)
time.sleep(2)

xpath = driver.find_element_by_xpath('//INPUT[@id="password"]')
xpath.send_keys(passwordd)
time.sleep(2)

xpath = driver.find_element_by_xpath('//BUTTON[@type="submit"][text()="Ingresar"]')
xpath.click()
time.sleep(3)


xpath = driver.find_element_by_xpath('//*[@id="dropdown-user-menu"]/div/button[2]')
xpath.click()
time.sleep(7)

xpath = driver.find_element_by_xpath('//SPAN[@_ngcontent-c1=""][text()="SMSi"]')
xpath.click()
time.sleep(6)

celu = '925266696'
mensaje = 'prueba77'

xpath = driver.find_element_by_xpath('//INPUT[@id="inputGsmList"]')
xpath.send_keys(celu)
time.sleep(6)

xpath = driver.find_element_by_xpath('//TEXTAREA[@id="txtMessage"]')
xpath.send_keys(mensaje)
time.sleep(6)


xpath = driver.find_element_by_xpath('//BUTTON[@id="buttonProcess"]')
xpath.click()
time.sleep(5)

xpath = driver.find_element_by_xpath('//*[@id="buttonSend"]')
xpath.click()
time.sleep(5)

driver.quit()





