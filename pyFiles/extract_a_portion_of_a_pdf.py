from PyPDF2 import PdfFileReader, PdfFileWriter

path = r"practice_files\Pride and Prejudice.pdf"

input_pdf = PdfFileReader(path)
output_pdf = PdfFileWriter()

# Gets the first page.
cover_page = input_pdf.getPage(0)
# And adds it to the PdfFileWriter object.
output_pdf.addPage(cover_page)

### wb = Write Binary
with open("Sliced and Diced.pdf", "wb") as output_file:
    output_pdf.write(output_file)