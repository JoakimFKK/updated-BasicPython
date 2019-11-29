# Fra package, brug Library
from PyPDF2 import PdfFileReader

path = r"practice_files\Pride and Prejudice.pdf"

def first_try():
    input_pdf = PdfFileReader(path)
    print(input_pdf.getNumPages())
    doc_info = input_pdf.getDocumentInfo()

    page0 = input_pdf.getPage(0)
    page0_text = input_pdf.getPage(0).extractText()
    print(page0_text)

    page_counter = 0
    for page in input_pdf.pages:
        print(page_counter)
        page_counter += 1

### REAL PYTHON Putting It All Together
def putting_it_all_together():
    input_pdf = PdfFileReader(path)
    ### få fat i meta data
    title = input_pdf.getDocumentInfo().title
    num_pages = input_pdf.getNumPages()

    # 2
    ### Opret ny txt som der skrives i, starter med metadata, efterfulgt af alle siderne (Dårligt formatteret)
    with open("Pride and Prejudice.txt", "w") as output_file:
        output_file.write(f"{title}\n")
        output_file.write(f"Numer of pages: {num_pages}\n\n")
        
        # 3
        for page in input_pdf.pages:
            text = page.extractText()
            output_file.write(text)

    print("Done")