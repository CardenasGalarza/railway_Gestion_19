import glob
import os
import time

import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

options = Options()
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-features=VizDisplayCompositor")


def delete_selenium_log():
    if os.path.exists('selenium.log'):
        os.remove('selenium.log')


def show_selenium_log():
    if os.path.exists('selenium.log'):
        with open('selenium.log') as f:
            content = f.read()
            st.code(content)


# not required anymore:
# def get_chromedriver_path():
#     results = glob.glob('/**/chromedriver', recursive=True)  # workaround on streamlit sharing
#     return results[0]


def run_selenium():
    name = str()
    with webdriver.Chrome(options=options, service_log_path='selenium.log') as driver:


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
        time.sleep(7)

        liddni3 = driver.find_element_by_xpath('//SPAN[@_ngcontent-c1=""][text()="SMSi"]')
        liddni3.click()
        time.sleep(6)


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

        # Wait for the element to be rendered:
        element = WebDriverWait(driver, 10).until(lambda x: x.find_elements(by=By.XPATH, value=xpath))
        name = element[0].get_property('attributes')[0]['name']
    return name



st.balloons()
if st.button('Start Selenium run'):
    st.info('Selenium is running, please wait...')
    result = run_selenium()
    st.info(f'Result -> {result}')
    st.info('Successful finished. Selenium log file is shown below...')
    #show_selenium_log()