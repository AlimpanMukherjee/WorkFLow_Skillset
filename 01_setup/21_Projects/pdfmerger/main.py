from PyPDF2 import PdfMerger

merger = PdfMerger()

n = int(input("Enter the number of PDF files you want to merge: "))
pdfnamelist = []

for i in range(n):
    pdfname = input(f"Enter the name of PDF {i+1} (with .pdf extension): ")
    pdfnamelist.append(pdfname)

for pdf in pdfnamelist:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()

print("✅ PDFs merged successfully into 'merged-pdf.pdf'")