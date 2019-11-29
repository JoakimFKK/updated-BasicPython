from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import copy

path = r"practice_files\half and half.pdf"
input_pdf = PdfFileReader(path)
output_pdf = PdfFileWriter()

for page_num in range(0, input_pdf.getNumPages()):
    # Page_left/right har nu begge en kopi af siden
    page_left = input_pdf.getPage(page_num)
    page_right = copy.copy(page_left)

    # Finder midten af siden
    upper_right = page_left.mediaBox.upperRight
    new_coords = (upper_right[0] / 2, upper_right[1])

    # Sætter top højre hjørne på venstre side
    page_left.mediaBox.upperRight = new_coords
    output_pdf.addPage(page_left)
    
    # sætter top venstre hjørne på højre side
    page_right.mediaBox.upperLeft = new_coords
    output_pdf.addPage(page_right)

output_path = "The Little Mermaid.pdf"
with open(output_path, "wb") as output_file:
    output_pdf.write(output_file)
    