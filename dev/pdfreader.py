import PyPDF2

O = open("BasicSet.pdf", "rb")
reader = PyPDF2.PdfFileReader(O)
page = reader.getPage(35)
print(page.extractText())
O.close()
