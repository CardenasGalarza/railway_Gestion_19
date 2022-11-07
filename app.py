import streamlit as st
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


st.title("Test Selenium")
st.markdown("You should see some random Football match text below in about 21 seconds")

firefoxOptions = Options()
firefoxOptions.add_argument("--headless")
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(
    options=firefoxOptions,
    service=service,
)

username = 'caramburu_TDP'
passwordd = 'WebSys29*T*'

driver.get("https://auth.movistaradvertising.com/login?logout")
time.sleep(3)

xpath = driver.find_element_by_xpath('//INPUT[@id="username"]')
xpath.send_keys(username)
time.sleep(6)

xpath = driver.find_element_by_xpath('//INPUT[@id="password"]')
xpath.send_keys(passwordd)
time.sleep(6)

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