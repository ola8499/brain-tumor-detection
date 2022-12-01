import tensorflow as tf
import re
from tensorflow import keras
import numpy as np
import streamlit as st
import os
from detection import detect_tumor
from report import create_report, create_download_link
from datetime import datetime
# from create_email import send_email
import sys, runpy
from multiprocessing import Process, Queue
import win32com.client as win32
import argparse
from instruction import open_instruction

parser = argparse.ArgumentParser()

tab1, tab2, tab3 = st.tabs(["Detector", "Instruction", "Documentation"])

with tab1:
    st.title("Brain Tumor Detector")

    image_file = st.file_uploader("Upload Image", type=['png', 'jpeg', 'jpg'], key="uploader",
                                  disabled=st.session_state.get("disabled", True))

    # sidebar
    with st.sidebar:
        regex_mail = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        regex_name = r'^[a-zA-Z]{4,}(?: [a-zA-Z]+){0,2}$'


        def clear_form():
            if re.fullmatch(regex_mail, st.session_state["email"]):
                st.session_state.disabled = False
            else:
                st.session_state["name"] = ""
                st.session_state["surname"] = ""
                st.session_state["id"] = ""
                st.session_state["email"] = ""


        with st.form("myform"):
            st.write("Type a Patient's data")
            name = st.text_input("Patient's First Name", key="name").title()
            surname = st.text_input("Patient's Surname", key="surname").title()
            id = st.text_input("Personal ID Number", key="id")
            email = st.text_input("Email Address", key="email")
            submit = st.form_submit_button(label="Submit", on_click=clear_form)

    if image_file is not None:

        folder = 'tmp-files'

        for file_name in os.listdir(folder):
            file = folder + "/" + file_name
            os.remove(file)

        file_details = {"Filename": image_file.name, "FileType": image_file.type, "FileSize": image_file.size}
        with open(os.path.join(folder, image_file.name), 'wb') as f:
            f.write(image_file.getbuffer())

        img = f.name
        result_container = st.container()
        col1, col2 = st.columns([20, 20])
        with result_container:
            with col1:
                st.image(img, width=300)
            with col2:
                detector = detect_tumor(img)
                percent = round(detector[1], 2)
                st.write(name + " " + surname + " " + detector[0], "with", str(percent), "% confidence.")
        btn_container = st.container()
        btn1, btn2 = st.columns([20, 20])
        with btn_container:
            with btn1:
                raport = st.button("Create PDF")
                if raport:
                    html = create_report(name,surname, id, detector, percent, img)
                    st.markdown(html, unsafe_allow_html=True)
            with btn2:
                send = st.button("Send by email")
                if send:
                    detectorpatient = detector[0].split()
                    print(os.system(f"python create_email.py {email} {name} {surname} {id} {detectorpatient[0]} {percent}"))


with tab2:
    st.header("Instruction")
    open_instruction()

with tab3:
    st.header("Documentation")

# st.session_state["id"].isnumeric() and len(st.session_state["id"])== 11 and  and re.fullmatch(regex_name, st.session_state["name"].strip())

