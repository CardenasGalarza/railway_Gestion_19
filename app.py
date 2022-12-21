import streamlit as st
import pickle
from pathlib import Path
import pandas as pd
import numpy as np
#from soupsieve import select  # pip install pandas openpyxl
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
############################################ OCULTAR INFROMACION NO IMPORTANTE
import base64
import streamlit as st
############################################ OCULTAR INFROMACION NO IMPORTANTE
import warnings
warnings.filterwarnings('ignore')
#########################################3333
##########################
from datetime import datetime
import gspread
#import pyautogui
from pkg_resources import working_set
import os

st.set_page_config(page_title='bdtickets-Averias', page_icon="🌀", layout='centered', initial_sidebar_state='auto')


st.sidebar.subheader("Cargar datos de acuerdo a lo requerido")

        # Setup file upload
uploaded_file = st.sidebar.file_uploader(
                        label="Solo cargar data TT y CMR. (200MB max)",
                        type=['csv', 'xlsx', 'XLS'])

global df
if uploaded_file is not None:
    #print(uploaded_file)
    #print("hello")

    with st.spinner('Procesando los datos...'):

        try:
            #df = pd.read_excel('dic_20_Copia de PasaParametros.xlsx', sheet_name = 'Para Liquidar', skiprows = 15, usecols = 'B').iloc[:-1]
            df = pd.read_excel(uploaded_file, engine="openpyxl", sheet_name = 'Para Liquidar', skiprows = 15, usecols = 'B').iloc[:-1]
            #https://es.stackoverflow.com/questions/350681/como-extraer-tablas-de-un-excel-para-cruzar-con-otra-base-de-excel-en-python
            #df = pd.read_excel('CARGARGILLERMO.xlsx')
            columdf = len(df.columns)
            print(columdf)

            if columdf == 1:

                now = datetime.today().strftime('%Y-%m-%d')

                df['fecha'] = np.nan
                df['fecha'] = df['fecha'].fillna(now)

                df.columns = ['codliq', 'fecha']

                #print(df)

                df = df.fillna('')
                df["codliq"]=df["codliq"].astype(str)

                gc = gspread.service_account(filename='datacargar-947843f340e2.json')
                sh = gc.open("guille_app")

                #  el 0 simbol del numero de hoja en este caso es la primera hoja = 0
                worksheet = sh.get_worksheet(0)

                df1 = pd.DataFrame(worksheet.get_all_records())


                df1["codliq"]=df1["codliq"].astype(str)
                #######
                ## TODO UNIR BASE DE DATOS MYSQL Y GOOGLE
                #######
                union = pd.concat([df, df1])
                #print(len(union))
                union = union.drop_duplicates(subset=['codliq'])

                union = union.sort_values(by='fecha')
                #borrar datos total y dejar encabezado
                worksheet.resize(rows=1)
                worksheet.resize(rows=30)
                #cargar datos df
                worksheet.update([union.columns.values.tolist()] + union.values.tolist())


        except Exception as e:
            st.error('DATA NO CORRESPONDE 👋🏻')

## fondo total
def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://cdn.pixabay.com/photo/2018/11/13/18/06/mail-3813618_960_720.jpg 1x, https://cdn.pixabay.com/photo/2018/11/13/18/06/mail-3813618_1280.jpg");
            background-attachment: fixed;
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_from_url()

st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')
st.sidebar.markdown('')

st.sidebar.markdown(
'<p class="big-font"; style="text-align:center;color:Lime;font-size:16px;border-radius:2%;">©👨🏻‍💻Giancarlos .C</p>', unsafe_allow_html=True
)
