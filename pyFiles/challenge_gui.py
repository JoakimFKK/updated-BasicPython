import os
from PyPDF2 import PdfFileReader as pdf_reader, PdfFileWriter as pdf_writer
import easygui as gui

input_file = gui.fileopenbox(title="Choose a PDF...", filetypes="*.pdf")
if input_file is None:
    exit(0)

pdfreader = pdf_reader(input_file)
pdfwriter = pdf_writer()
pdf_total_pages = pdfreader.getNumPages()

while True:
    try:
        input_starting_page = int(gui.enterbox("Write a valid starting page: "))
        if input_starting_page < 0 and input_starting_page < pdf_total_pages:
            gui.msgbox("Input out of range")
            continue
        while True:
            try:
                input_ending_page = int(gui.enterbox("Write a valid ending page: "))
                if input_ending_page >= input_starting_page and input_ending_page <= pdf_total_pages:
                    break
                continue
            except ValueError:
                gui.msgbox(msg="Invalid user input(end)!", title="Error!")
        break
    except ValueError:
        gui.msgbox(msg="Invalid user input(start)!", title="Error!")

output_file = gui.filesavebox(title="Choose the location for the new file...", default=input_file)
if output_file is None:
    exit(0)
elif output_file[:-4].lower() != ".pdf":
    output_file += ".pdf"

print(input_starting_page, input_ending_page, sep=" - ")
for i in range(input_starting_page, input_ending_page):
    pdfwriter.addPage(pdfreader.getPage(i - 1))

with open(output_file, "wb") as modified_pdf:
    pdfwriter.write(modified_pdf)