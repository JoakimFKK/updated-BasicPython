from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import copy

walrus_path = "practice_files/Walrus.pdf"

reader_pdf = PdfFileReader(walrus_path)
writer_pdf = PdfFileWriter()

reader_pdf.decrypt("IamtheWalrus")

for page in range(0, reader_pdf.getNumPages()):
    # Page split and rotating
    left_page = reader_pdf.getPage(page).rotateClockwise(-90)
    right_page = copy.copy(left_page)
    # where does the page end?
    upper_right = right_page.mediaBox.upperRight
    # Horizontal -> vertical
    split_page = (upper_right[0] / 2, upper_right[1])
    # Ændrer side koordinater
    left_page.mediaBox.upperRight = split_page
    right_page.mediaBox.upperLeft = split_page
    # Tilføjer siderne til writer_pdf
    writer_pdf.addPage(left_page)
    writer_pdf.addPage(right_page)

with open("I am the walrus.pdf", "wb") as output_file:
    writer_pdf.write(output_file)
