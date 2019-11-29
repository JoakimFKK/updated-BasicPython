from PyPDF2 import PdfFileWriter, PdfFileReader
import os

path = "practice_files"

input_file_path = os.path.join(path, "The Emperor.pdf")
input_pdf = PdfFileReader(input_file_path)
output_pdf = PdfFileWriter()

watermark_file_path = os.path.join(path, "top secret.pdf")
watermark_pdf = PdfFileReader(watermark_file_path)
watermark_page = watermark_pdf.getPage(0)

for page in input_pdf.pages:
    page.mergePage(watermark_page)
    output_pdf.addPage(page)

# output_file_path = os.path.join(path, "New Suit.pdf")
with open("new suit.pdf", "wb") as output_file:
    output_pdf.write(output_file)