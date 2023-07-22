from PyPDF2 import PdfMerger

# create an object of the class
pdfmerger = PdfMerger()

# create a list of files with file paths you want to merge
pdf_files = ["C:/Users/dhruv/OneDrive/Documents/3130008.pdf","C:/Users/dhruv/OneDrive/Documents/3150709 (1).pdf"]

# itterate over file paths and append or merge files
for files in pdf_files:
    pdfmerger.append(files)

pdfmerger.write("Merged_files.pdf")

pdfmerger.close()