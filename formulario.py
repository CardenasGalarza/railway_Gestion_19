import streamlit as st
import streamlit as st
from streamlit_option_menu import option_menu
import pickle
from pathlib import Path
import pandas as pd
import numpy as np
#from soupsieve import select  # pip install pandas openpyxl
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
############################################ OCULTAR INFROMACION NO IMPORTANTE
import base64
import mysql.connector
from mysql.connector import Error
#import pyodbc
import streamlit as st
############################################ OCULTAR INFROMACION NO IMPORTANTE
import warnings
warnings.filterwarnings('ignore')
#########################################3333
##########################
import time
from datetime import datetime
from datetime import timedelta
import gspread
import re


with st.form("my_form"):

    col1, col2, col3 , col4, col5 = st.columns(5)

    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col1:
        celu = st.text_input('Numero')
    filter_type8 = st.selectbox(
        "Mensaje",
        (
            "Gracias por llamar a mi empresa",
            "Has llegado a mi empresa. Tu llamada es importante para nosotros",
            "7C_TEMA COMERCIALES",
            "7D_GENERA NUEVO REQ",
            #"7E_NO SE UBICA CLITE",
            "7F_REQ MAL GENERADO",
            "Requiere Visita Tecnica",
            "En espera",
        ),
        key="filter_type8",
        help="""
        Ten encuenta tu accion `Ticket` inf.
        """,
    )


    #TODO SIVERVPARA BARRA AZUL
    #celu = '925266696'
    #print(celu)

    #title = st.text_input("INGRESA TU GESTION")
    mensaje = filter_type8



    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")

    if submitted == True:
        import streamlit as st
        import glob
        import os
        import time

        import streamlit as st
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.common.by import By

        options = Options()
        options.add_argument("--headless")
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
        #st.button("Inicio")
        col1, col2, col3 , col4, col5 = st.columns(5)

        with col1:
            pass
        with col2:
            pass
        with col4:
            pass
        with col1:
            pass
        with col5 :
            st.balloons()

        

        driver = webdriver.Chrome(options=options, service_log_path='selenium.log')

        username = 'caramburu_TDP'
        passwordd = 'WebSys29*T*'
        driver.get("https://auth.movistaradvertising.com/login?logout")
        time.sleep(1)

        st.success('listoooooooo')
        time.sleep(2)
        st.balloons()
        import pyautogui
        pyautogui.hotkey("ctrl","F5")

        

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

        #celu = '925266696'
        #mensaje = 'Listoooossdddssss'

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



with st.form("ssss"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")
    

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
st.write("Outside the form")


name = st.text_input('Name')
if not name:
  st.warning('Please input a name.')
  st.stop()
st.success('Thank you for inputting a name.')