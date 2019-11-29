import os
from PyPDF2 import PdfFileReader, PdfFileWriter

"""
    PDF encryptering
"""
def pdf_encrypting():
    path = "new suit.pdf"
    input_pdf = PdfFileReader(path)
    output_pdf = PdfFileWriter()

    for page in input_pdf.pages:
        output_pdf.addPage(page)

    output_pdf.encrypt("SuperSecret")

    with open("newest suit.pdf", "wb") as output_file:
        output_pdf.write(output_file)

def pdf_decrypting():
    path = "newest suit.pdf"
    input_pdf = PdfFileReader(path)

    input_pdf.decrypt("SuperSecret")

    for page in input_pdf.pages:
        text = page.extractText()
        print(text)