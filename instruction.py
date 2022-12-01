from PIL import Image
import streamlit as st


def open_instruction():
    st.markdown("Brain Tumor Detector is application for detection on your own images a brain tumor.")
    image1 = Image.open('instruction/1.PNG')
    st.image(image1, caption='The main screen of application.')

    st.markdown("In the upper right corner there is a built-in Menu. This button is from Streamlit.")
    image2 = Image.open("instruction/2.png")
    st.image(image2, caption='The main menu.')

    st.header("Start detecting brain tumors!")
    st.subheader("1. Fill all the inputs available on the left side.")

    st.markdown("Enter the patient's name, surname, number ID and e-mail address.")
    image3 = Image.open("instruction/3.png")
    st.image(image3, caption="Form to be completed before detection.")

    st.subheader("2. Submit your data.")

    st.markdown("After pressing the 'submit' button, your data will be saved.")
    image4 = Image.open("instruction/4.png")
    st.image(image4, caption="Submit button.")

    st.markdown("A place where you can upload your image becomes available.")
    image7 = Image.open("instruction/7.png")
    st.image(image7, caption="Available uploader.")

    st.subheader("3. Upload image by pressing the button or using drag and drop option.")

    st.markdown("Press \"Browse files\" to upload image from your own device.")
    image8 = Image.open("instruction/8.png")
    st.image(image8, caption="'Browse files' button.")

    st.markdown("Drag and drop your image in this place.")
    image9 = Image.open("instruction/10.png")
    st.image(image9, caption="Drag and drop option.")

    st.markdown("Application screen should looks like this.")
    image10 = Image.open("instruction/11.PNG")
    st.image(image10, caption="Application screen after uploading the image.")

    st.markdown("On he right is the result of detection.")
    image11 = Image.open("instruction/12.png")
    st.image(image11, caption="Result")

    st.subheader("4. Create a PDF file with the result of detection.")

    st.markdown("To prepare the report, press the \"Create PDF\" button.")
    image12 = Image.open("instruction/13.png")
    st.image(image12, caption="Create PDF.")

    st.markdown("To download the report, press the \"Download file\".")
    image13 = Image.open("instruction/14.PNG")
    st.image(image13, caption="Download PDF.")

    st.subheader("4. Send the result of detection.")

    st.markdown("To send the result, press the \"Send by email\".")
    image14 = Image.open("instruction/16.PNG")
    st.image(image14, caption="Send the result.")


