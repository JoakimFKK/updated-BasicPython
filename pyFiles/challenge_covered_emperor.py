from PyPDF2 import PdfFileReader, PdfFileWriter

### Locations
cover_path = "practice_files/Emperor cover sheet.pdf"
story_path = "practice_files/The Emperor.pdf"

## Opretter to PdfFileReaders for hver pdf
cover_reader = PdfFileReader(cover_path)
story_reader = PdfFileReader(story_path)
pdf_writer = PdfFileWriter()

## Kun en side som kan vælges, men kan sættes i loop hvis behov.
pdf_writer.addPage(cover_reader.getPage(0))

## tilføjer alle siderne efter cover
for num_page in range(0, story_reader.getNumPages()):
    pdf_writer.addPage(story_reader.getPage(num_page))

## udprint
with open("The Covered Emperor.pdf", "wb") as output_file:
    pdf_writer.write(output_file)