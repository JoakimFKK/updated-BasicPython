from PyPDF2 import PdfFileReader, PdfFileWriter

path = r"practice_files\The Whistling Gypsy.pdf"

input_pdf = PdfFileReader(path)
print("Title:", input_pdf.getDocumentInfo().title)
print("Author:", input_pdf.getDocumentInfo().author)
print("Number of pages:", input_pdf.getNumPages())

# print(f"'{input_pdf.getDocumentInfo().title}' by {input_pdf.getDocumentInfo().author}. {input_pdf.getNumPages()} pages long.")

with open("WhistlingSlur.txt", "w") as output_file:
    for page in range(0, input_pdf.getNumPages()):
        text = input_pdf.getPage(page).extractText()
        output_file.write(str(text.encode("utf-8")))