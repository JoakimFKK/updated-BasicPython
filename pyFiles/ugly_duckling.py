from PyPDF2 import PdfFileReader, PdfFileWriter

path = r"C:\Users\joak\source\repos\Python\Ch00 - Exercise files\ch13-interact-with-pdf-files\practice_files\ugly.pdf"

input_pdf = PdfFileReader(path)
output_pdf = PdfFileWriter()

### Gør klar til loop som kører baseret på hvor mange sider der er. 
total_pages = input_pdf.getNumPages()
for n in range(0, total_pages):
    page = input_pdf.getPage(n)
    if n % 2 == 0:
        page.rotateClockwise(90)
    output_pdf.addPage(page)

with open("The Conformed Duckling.pdf", "wb") as output_file:
    output_pdf.write(output_file)