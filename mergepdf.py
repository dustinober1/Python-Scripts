from PyPDF2 import PdfMerger

pdfs = ["file1.pdf", "file2.pdf", "file3.pdf"]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged_files.pdf")
merger.close()
