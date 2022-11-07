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

URL = ""
TIMEOUT = 20

st.title("Test Selenium")

firefoxOptions = Options()
firefoxOptions.add_argument("--headless")
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(
    options=firefoxOptions,
    service=service,
)
driver.get('https://auth.movistaradvertising.com/login?logout')



username = 'caramburu_TDP'
passwordd = 'WebSys29*T*'


xpath = driver.find_element_by_xpath('//INPUT[@id="username"]')
xpath.send_keys(username)
time.sleep(2)

xpath = driver.find_element_by_xpath('//INPUT[@id="password"]')
xpath.send_keys(passwordd)
time.sleep(2)

