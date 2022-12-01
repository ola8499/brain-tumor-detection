from datetime import datetime
from fpdf import FPDF
import base64
import os


def create_report(name, surname, pesel, detector, percent, img):
    for file_name in os.listdir('pdf-files'):
        file = 'pdf-files' + "/" + file_name
        os.remove(file)
    pdf = FPDF()
    now = datetime.now()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.image('HealthBrain(1).png', 10, 8, 25)
    pdf.set_font('Arial', 'BU', 20)
    pdf.cell(80)
    pdf.cell(30, 15, 'Brain Tumor Detection', 0, 0, 'C')
    pdf.ln(20)

    pdf.set_font('Times', 'BU', 16)
    pdf.cell(0, 10, 'Patient data: ', 0, 1)
    pdf.set_font('Times', '', 16)
    pdf.cell(0, 10, "Full Name: " + name + " " + surname, 0, 1)
    pdf.cell(0, 10, "PESEL: " + pesel, 0, 1)
    pdf.cell(0, 10, "Date: " + now.strftime("%d/%m/%Y %H:%M:%S"), 0, 1)
    pdf.ln(7)
    pdf.set_font('Times', 'B', 18)
    pdf.cell(0, 10, "Result:", 0, 1)
    pdf.set_font('Times', '', 16)
    pdf.cell(0, 10,
             "Patient " + name + " " + surname + " " + str(detector[0]) + " with " + str(percent) + "% confidence.", 0,
             1)
    pdf.image(img, w=70)

    html = create_download_link(pdf.output(dest="S"), "BTD-result")
    file = pdf.output('pdf-files/BTD-result.pdf', 'F')
    return html


def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'


