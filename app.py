import streamlit as st
from dateutil.parser import parse
import streamlit.components.v1 as components
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


st.title("Auto Search App")

driver = webdriver.Chrome(ChromeDriverManager().install())

wait = WebDriverWait(driver, 20)

# url = 'https://wego.here.com/'
# driver.get(url)

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